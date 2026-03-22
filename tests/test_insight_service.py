from __future__ import annotations

from pathlib import Path

import pandas as pd

from biomed_api.models.schemas import ChartArtifact
from biomed_api.services.insight_service import generate_insights_bundle, read_final_insights


def _build_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "age_months": [12, 24, 18, 36, 30],
            "stage": ["2", "4", "3", "4", "2"],
            "risk_group": ["low", "high", "intermediate", "high", "low"],
            "efs_months": [30, 12, 20, 8, 28],
            "event": [0, 1, 0, 1, 0],
            "mycn_amplified": [0, 1, 0, 1, 0],
            "expr_mycn": [1.2, 2.7, 1.8, 3.1, 1.4],
            "expr_alk": [1.9, 1.2, 1.5, 1.1, 1.8],
            "expr_mdm2": [1.1, 2.4, 1.9, 2.8, 1.3],
        }
    )


def test_generate_insights_bundle_writes_markdown_and_html(tmp_path: Path) -> None:
    df = _build_df()
    artifacts = [
        ChartArtifact(
            name="biomarker_correlation_heatmap.png",
            category="biomarker",
            format="png",
            path=str(tmp_path / "images" / "biomarker_correlation_heatmap.png"),
        ),
        ChartArtifact(
            name="clinical_risk_distribution.png",
            category="clinical",
            format="png",
            path=str(tmp_path / "images" / "clinical_risk_distribution.png"),
        ),
    ]

    insights_md, insights_html, section_paths = generate_insights_bundle(
        df, artifacts, insights_dir=tmp_path / "insights"
    )

    assert insights_md.exists()
    assert insights_html.exists()
    assert len(section_paths) == 2
    for section_path in section_paths:
        content = section_path.read_text(encoding="utf-8")
        assert "## Medical Insight" in content
        assert "## Research Insight" in content
        assert "![" in content


def test_read_final_insights_returns_path_and_content(tmp_path: Path) -> None:
    insights_path = tmp_path / "insights.md"
    insights_path.write_text("# Final Biomedical Insights\n", encoding="utf-8")

    path, content = read_final_insights(insights_path=insights_path)

    assert path == insights_path
    assert "Final Biomedical Insights" in content
