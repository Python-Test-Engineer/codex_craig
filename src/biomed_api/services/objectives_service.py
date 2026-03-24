from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from biomed_api.models.schemas import ChartArtifact


OBJECTIVES_PATH = Path("OBJECTIVES.md")
RESPONSE_PATH = Path("output/RESPONSE_TO_OBJECTIVES.md")


def _parse_objectives(text: str) -> list[str]:
    """Extract bullet/numbered lines from objectives markdown."""
    objectives: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            objectives.append(stripped[2:].strip())
        elif stripped and stripped[0].isdigit() and "." in stripped[:4]:
            objectives.append(stripped.split(".", 1)[-1].strip())
    return objectives


def _extract_report_bullets(report_text: str) -> list[str]:
    bullets: list[str] = []
    for line in report_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped[2:].strip())
    return bullets


def _match_finding(objective: str, bullets: list[str]) -> list[str]:
    """Return report bullets whose keywords overlap with the objective."""
    obj_tokens = set(objective.lower().replace(",", " ").split())
    stopwords = {"a", "an", "the", "and", "or", "of", "to", "in", "for", "is", "are", "be", "by", "with"}
    obj_tokens -= stopwords

    matched: list[str] = []
    for bullet in bullets:
        b_tokens = set(bullet.lower().split())
        if obj_tokens & b_tokens:
            matched.append(bullet)
    return matched


def generate_response_to_objectives(
    chart_artifacts: list[ChartArtifact],
    objectives_path: Path | None = None,
    response_path: Path | None = None,
) -> Path:
    obj_path = objectives_path or OBJECTIVES_PATH
    out_path = response_path or RESPONSE_PATH
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Read objectives
    if obj_path.exists():
        obj_text = obj_path.read_text(encoding="utf-8")
    else:
        obj_text = ""

    objectives = _parse_objectives(obj_text)

    # Read report findings
    report_path = Path("output/report.md")
    report_text = report_path.read_text(encoding="utf-8") if report_path.exists() else ""
    report_bullets = _extract_report_bullets(report_text)

    # Read insights summary
    insights_path = Path("output/insights/insights.md")
    insights_text = insights_path.read_text(encoding="utf-8") if insights_path.exists() else ""
    insights_bullets = _extract_report_bullets(insights_text)

    generated_at = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = [
        "# Response to Objectives",
        "",
        f"Generated: {generated_at}",
        "",
        "---",
        "",
    ]

    if not objectives:
        lines += [
            "> No objectives were found in OBJECTIVES.md.",
            "> Please add bullet points or numbered items to define your objectives.",
            "",
        ]
    else:
        lines += [
            f"This document maps the pipeline outputs to each of the {len(objectives)} stated objectives.",
            "",
        ]
        for i, obj in enumerate(objectives, 1):
            lines += [f"## Objective {i}", "", f"> {obj}", ""]

            # Match report findings
            report_matches = _match_finding(obj, report_bullets)
            insights_matches = _match_finding(obj, insights_bullets)

            if report_matches or insights_matches:
                lines.append("**Addressed by pipeline findings:**")
                lines.append("")
                for m in report_matches[:3]:
                    lines.append(f"- {m}")
                for m in insights_matches[:2]:
                    lines.append(f"- *(Insight)* {m}")
                lines.append("")
            else:
                lines.append("**Status:** No direct match found in current report/insights — further analysis may be required.")
                lines.append("")

            # Relevant charts
            obj_lower = obj.lower()
            keywords = {"biomarker": ["biomarker", "correlation", "expression"],
                        "survival": ["km", "efs", "survival"],
                        "risk": ["risk", "outcome"],
                        "clinical": ["age", "stage", "distribution", "clinical"]}
            relevant: list[str] = []
            for artifact in chart_artifacts:
                name_lower = artifact.name.lower()
                for kw_group, kw_list in keywords.items():
                    if any(k in obj_lower for k in kw_list) and any(k in name_lower for k in kw_list):
                        relevant.append(artifact.name)
                        break
            if relevant:
                lines.append("**Related charts:**")
                lines.append("")
                for r in relevant[:4]:
                    lines.append(f"- `{r}`")
                lines.append("")

    # Summary section
    lines += [
        "---",
        "",
        "## Pipeline Output Summary",
        "",
        f"- Charts generated: {len(chart_artifacts)}",
        f"- Report available: {'Yes' if report_text else 'No'}",
        f"- Insights available: {'Yes' if insights_text else 'No'}",
        f"- Objectives stated: {len(objectives)}",
        "",
        "## Caveats",
        "",
        "- Objective matching is keyword-based and exploratory.",
        "- All findings are non-causal and should be validated in an independent cohort.",
        "- This response was generated automatically from pipeline outputs.",
        "",
    ]

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path
