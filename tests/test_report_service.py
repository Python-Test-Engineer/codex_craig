from __future__ import annotations

from pathlib import Path

import pandas as pd

from biomed_api.services.chart_service import generate_standard_charts
from biomed_api.services.report_service import generate_report, read_report


def _build_report_df() -> pd.DataFrame:
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


def test_generate_report_writes_required_sections(tmp_path: Path) -> None:
    df = _build_report_df()
    charts = generate_standard_charts(df, output_dir=tmp_path, clean_output=True, write_png=False)

    report_path = tmp_path / "report.md"
    written = generate_report(df, charts, report_path=report_path)

    assert written.exists()
    content = written.read_text(encoding="utf-8")
    assert "## Cohort Snapshot" in content
    assert "## Outcome Stratification" in content
    assert "## Top Biomarker-EFS Associations" in content
    assert "## Chart Index" in content
    assert "## Caveats" in content


def test_read_report_returns_path_and_content(tmp_path: Path) -> None:
    report_path = tmp_path / "report.md"
    report_path.write_text("# test\n", encoding="utf-8")

    path, content = read_report(report_path=report_path)

    assert path == report_path
    assert "# test" in content
