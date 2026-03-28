from __future__ import annotations

import base64
import json
import logging
import os
import threading
from datetime import UTC, datetime
from pathlib import Path

import anthropic
import pandas as pd
from dotenv import load_dotenv

from csv_analyser.config import OUTPUT_DIR, PROJECT_ROOT
from csv_analyser.models.schemas import ChartArtifact
from csv_analyser.utils.html import render_markdown_to_html


logger = logging.getLogger(__name__)

INSIGHTS_DIR = OUTPUT_DIR / "insights"
FINAL_INSIGHTS_MD = INSIGHTS_DIR / "insights.md"
FINAL_INSIGHTS_HTML = INSIGHTS_DIR / "insights.html"
DOTENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=DOTENV_PATH, override=False)

MODEL = os.environ.get("OPENROUTER_INSIGHTS_MODEL", os.environ.get("OPENROUTER_MODEL", "anthropic/claude-3.5-sonnet"))
OPENROUTER_BASE_URL = "https://openrouter.ai/api"
MAX_TOKENS = 1_400


def _safe_title(stem: str) -> str:
    return stem.replace("_", " ").title()


def _dataset_snapshot(df: pd.DataFrame) -> list[str]:
    numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    lines: list[str] = [
        f"- Rows: {len(df)}",
        f"- Columns: {len(df.columns)}",
        f"- Numeric columns: {len(numeric_cols)}",
    ]
    for col in numeric_cols[:3]:
        series = pd.to_numeric(df[col], errors="coerce").dropna()
        if len(series) > 0:
            lines.append(f"- {col}: mean={series.mean():.2f}, std={series.std():.2f}")
    return lines


def _build_data_insight(name_stem: str, df: pd.DataFrame) -> str:
    numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    cat_cols = [
        c for c in df.columns
        if not pd.api.types.is_numeric_dtype(df[c])
        and not pd.api.types.is_datetime64_any_dtype(df[c])
        and 2 <= df[c].nunique() <= 50
    ]

    if "correlation_heatmap" in name_stem:
        if len(numeric_cols) >= 2:
            corr = df[numeric_cols].corr(numeric_only=True).abs()
            max_corr: float | None = None
            pair: tuple[str, str] = ("", "")
            for i, c1 in enumerate(corr.columns):
                for c2 in corr.columns[i + 1:]:
                    val = corr.loc[c1, c2]
                    if pd.isna(val):
                        continue
                    if max_corr is None or float(val) > max_corr:
                        max_corr = float(val)
                        pair = (c1, c2)
            if max_corr is not None:
                return (
                    f"The strongest correlation is between '{pair[0]}' and '{pair[1]}' "
                    f"(r ≈ {max_corr:.2f}), suggesting these columns move together and may be related."
                )
        return "The correlation map shows how numeric columns co-vary, helping identify redundant or related features."

    if "overview_numeric" in name_stem:
        if numeric_cols:
            return (
                f"The dataset contains {len(numeric_cols)} numeric column(s). "
                "This chart compares their spread, helping spot outliers and scale differences."
            )
        return "This chart summarises the numeric columns in the dataset."

    if "distribution_" in name_stem:
        col_hint = name_stem.replace("distribution_", "").replace("_", " ")
        return (
            f"The distribution of '{col_hint}' reveals the spread and shape of values. "
            "Skewed distributions or outliers may warrant transformation before modelling."
        )

    if "category_" in name_stem:
        col_hint = name_stem.replace("category_", "").replace("_", " ")
        if cat_cols:
            col_match = next((c for c in cat_cols if c.replace(" ", "_").lower() in name_stem), None)
            if col_match:
                top = df[col_match].value_counts().index[0]
                return (
                    f"'{top}' is the most frequent value in '{col_match}'. "
                    "Imbalanced categories may skew aggregates and require stratified analysis."
                )
        return f"The distribution of '{col_hint}' shows which values dominate this categorical column."

    if "time_series_" in name_stem:
        col_hint = name_stem.replace("time_series_", "").replace("_", " ")
        return (
            f"The monthly trend for '{col_hint}' highlights seasonality, growth, or decline patterns over time."
        )

    if "scatter" in name_stem:
        return (
            "This scatter plot reveals the relationship between two numeric columns. "
            "Clusters or linear trends can motivate correlation and regression analyses."
        )

    return "This chart provides exploratory context for understanding the dataset structure and distributions."


def _build_analysis_insight(name_stem: str, df: pd.DataFrame) -> str:
    if "correlation_heatmap" in name_stem:
        return "Use this map to reduce collinearity in downstream models and prioritise orthogonal feature subsets."
    if "overview_numeric" in name_stem:
        return "Consider normalising or scaling columns with very different ranges before applying distance-based algorithms."
    if "distribution_" in name_stem:
        return "Highly skewed distributions may benefit from log or Box-Cox transformation before statistical modelling."
    if "category_" in name_stem:
        return "Rare categories can be grouped into an 'Other' bucket to reduce noise and improve model generalisation."
    if "time_series_" in name_stem:
        return "Decompose the series into trend, seasonality, and residual components to improve forecasting accuracy."
    if "scatter" in name_stem:
        return "The bivariate structure can motivate interaction terms and subgroup analyses in regression models."
    return "This chart supports exploratory hypothesis generation and should be validated on a held-out subset."


def _build_caveat(df: pd.DataFrame) -> str:
    missing = int(df.isna().sum().sum())
    return (
        f"Insights are exploratory and non-causal. Missing cells in source data: {missing}. "
        "Sample size, data quality, and unmeasured variables may affect conclusions."
    )


def _extract_response_text(response: object) -> str:
    content = getattr(response, "content", [])
    for block in content:
        if getattr(block, "type", "") == "text":
            return getattr(block, "text", "")
    return ""


def _extract_json_payload(text: str) -> dict[str, str] | None:
    try:
        payload = json.loads(text)
        if isinstance(payload, dict):
            return payload
    except json.JSONDecodeError:
        pass

    marker = "```json"
    if marker in text and "```" in text[text.find(marker) + len(marker):]:
        start = text.find(marker) + len(marker)
        end = text.find("```", start)
        snippet = text[start:end].strip()
        try:
            payload = json.loads(snippet)
            if isinstance(payload, dict):
                return payload
        except json.JSONDecodeError:
            return None
    return None


def _dataset_context_for_prompt(df: pd.DataFrame) -> str:
    numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    lines = [
        f"Rows: {len(df)}",
        f"Columns: {len(df.columns)}",
        f"Column names: {', '.join(df.columns.tolist())}",
    ]
    for col in numeric_cols[:4]:
        series = pd.to_numeric(df[col], errors="coerce").dropna()
        if len(series) > 0:
            lines.append(f"{col}: mean={series.mean():.2f}, std={series.std():.2f}")
    return "\n".join(lines)


def _generate_llm_insights(
    *,
    stem: str,
    image_path: Path,
    df: pd.DataFrame,
    api_key: str,
    cancel_event: threading.Event | None = None,
) -> dict[str, str]:
    system_prompt = """\
You are a senior data analyst.
You are given one chart image and dataset metadata.
Return only strict JSON with these string fields:
- data_insight
- analysis_insight
- caveat

Rules:
- Base claims on visible chart structure and provided dataset context.
- Keep each field <= 90 words.
- Avoid causal claims and avoid fabricated p-values/effect sizes.
- caveat must mention uncertainty, confounding, or data quality limits.
"""
    user_text = f"""\
Chart file stem: {stem}

Dataset context:
{_dataset_context_for_prompt(df)}

Write concise, chart-specific insights now in strict JSON only.
"""

    client = anthropic.Anthropic(
        api_key=api_key,
        base_url=OPENROUTER_BASE_URL,
        timeout=25.0,
    )
    text_only_blocks: list[dict[str, object]] = [{"type": "text", "text": user_text}]

    def _call_streaming(blocks: list[dict[str, object]]) -> dict[str, str]:
        """Stream response token-by-token, checking for cancellation between chunks."""
        raw_text = ""
        with client.messages.stream(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system_prompt,
            messages=[{"role": "user", "content": blocks}],
        ) as stream:
            for chunk in stream.text_stream:
                if cancel_event and cancel_event.is_set():
                    raise RuntimeError("Pipeline cancelled.")
                raw_text += chunk
        payload = _extract_json_payload(raw_text)
        if payload is None:
            raise ValueError("LLM output was not valid JSON.")
        return payload

    payload: dict[str, str]
    if image_path.exists():
        image_bytes = image_path.read_bytes()
        image_b64 = base64.b64encode(image_bytes).decode("ascii")
        image_blocks = text_only_blocks + [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_b64,
                },
            }
        ]
        try:
            payload = _call_streaming(image_blocks)
        except RuntimeError:
            raise  # propagate cancellation
        except Exception:
            payload = _call_streaming(text_only_blocks)
    else:
        payload = _call_streaming(text_only_blocks)

    data_insight = str(payload.get("data_insight", "")).strip()
    analysis_insight = str(payload.get("analysis_insight", "")).strip()
    caveat = str(payload.get("caveat", "")).strip()
    if not data_insight or not analysis_insight or not caveat:
        raise ValueError("LLM output omitted one or more required fields.")
    return {
        "data_insight": data_insight,
        "analysis_insight": analysis_insight,
        "caveat": caveat,
    }



def generate_insights_bundle(
    df: pd.DataFrame,
    chart_artifacts: list[ChartArtifact],
    insights_dir: str | Path | None = None,
    cancel_event: threading.Event | None = None,
) -> tuple[Path, Path, list[Path]]:
    target_dir = Path(insights_dir) if insights_dir is not None else INSIGHTS_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    png_artifacts = [artifact for artifact in chart_artifacts if artifact.format == "png"]
    section_paths: list[Path] = []

    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    llm_enabled = bool(api_key)
    llm_failures: list[str] = []

    for artifact in png_artifacts:
        if cancel_event and cancel_event.is_set():
            raise RuntimeError("Pipeline cancelled.")
        stem = Path(artifact.name).stem
        section_path = target_dir / f"{stem}.md"
        image_rel_path = f"../images/{artifact.name}"
        image_path = Path(artifact.path)

        data_insight = _build_data_insight(stem, df)
        analysis_insight = _build_analysis_insight(stem, df)
        caveat = _build_caveat(df)

        if llm_enabled:
            try:
                generated = _generate_llm_insights(
                    stem=stem,
                    image_path=image_path,
                    df=df,
                    api_key=api_key,
                    cancel_event=cancel_event,
                )
                data_insight = generated["data_insight"]
                analysis_insight = generated["analysis_insight"]
                caveat = generated["caveat"]
            except RuntimeError:
                raise  # propagate cancellation out of the loop
            except Exception as exc:
                logger.warning("LLM insight generation failed for %s: %s", artifact.name, exc)
                llm_failures.append(f"{artifact.name}: {exc}")

        lines = [
            f"# Insights: {_safe_title(stem)}",
            "",
            f"![{artifact.name}]({image_rel_path})",
            "",
            "## Data Insight",
            f"- {data_insight}",
            "",
            "## Analysis Insight",
            f"- {analysis_insight}",
            "",
            "## Caveat",
            f"- {caveat}",
            "",
        ]
        section_path.write_text("\n".join(lines), encoding="utf-8")
        section_paths.append(section_path)

    generated_at = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    merged_lines: list[str] = [
        "# Final Data Insights",
        "",
        f"- Generated: {generated_at}",
        f"- Model setting: {MODEL}",
        f"- LLM-enabled: {'yes' if llm_enabled else 'no'}",
        f"- Individual insight files: {len(section_paths)}",
        "",
        "## Dataset Context",
        *_dataset_snapshot(df),
        "",
        "## Consolidated Chart Insights",
        "",
    ]

    if llm_failures:
        merged_lines.extend(
            [
                "## Generation Notes",
                "- LLM generation failed for one or more charts; heuristic fallback was used.",
                *[f"- {item}" for item in llm_failures],
                "",
            ]
        )

    for section_path in section_paths:
        merged_lines.append(f"### {section_path.stem.replace('_', ' ').title()}")
        merged_lines.append("")
        merged_lines.append(section_path.read_text(encoding="utf-8").strip())
        merged_lines.append("")

    final_md_path = target_dir / FINAL_INSIGHTS_MD.name
    final_html_path = target_dir / FINAL_INSIGHTS_HTML.name
    final_md_path.write_text("\n".join(merged_lines) + "\n", encoding="utf-8")

    html_body = render_markdown_to_html(final_md_path.read_text(encoding="utf-8"))
    html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Final Data Insights</title>
  <style>
    body {{
      margin: 0;
      background: #f3f6f8;
      color: #102227;
      font-family: "Segoe UI", Arial, sans-serif;
    }}
    main {{
      width: min(980px, 100% - 28px);
      margin: 24px auto 40px;
      background: #ffffff;
      border: 1px solid #d8dfe6;
      border-radius: 14px;
      padding: 20px;
    }}
    h1, h2, h3 {{
      color: #0f3a47;
    }}
    p, li {{
      line-height: 1.5;
    }}
    ul {{
      padding-left: 20px;
    }}
    .toolbar {{
      display: flex;
      justify-content: flex-end;
      margin-bottom: 12px;
    }}
    .download-btn {{
      display: inline-block;
      text-decoration: none;
      background: #1f4a63;
      color: #ffffff;
      padding: 9px 12px;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
    }}
    .download-btn:hover {{
      opacity: 0.92;
    }}
  </style>
</head>
<body>
  <main>
    <div class="toolbar">
      <a class="download-btn" href="../report.md" download="report.md">Download Report</a>
    </div>
    {html_body}
  </main>
</body>
</html>
"""
    final_html_path.write_text(html_page, encoding="utf-8")
    return final_md_path, final_html_path, section_paths


def read_final_insights(insights_path: str | Path | None = None) -> tuple[Path, str]:
    target = Path(insights_path) if insights_path is not None else FINAL_INSIGHTS_MD
    if not target.exists() or not target.is_file():
        raise FileNotFoundError(f"Insights file not found at '{target}'.")
    return target, target.read_text(encoding="utf-8")
