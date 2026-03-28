from __future__ import annotations

from pathlib import Path

import pandas as pd

from csv_analyser.services.chart_service import generate_standard_charts, list_chart_artifacts


def _build_chart_df() -> pd.DataFrame:
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


def test_generate_standard_charts_creates_artifacts(tmp_path: Path) -> None:
    df = _build_chart_df()

    artifacts = generate_standard_charts(
        df, output_dir=tmp_path, clean_output=True, write_png=True
    )

    assert artifacts
    assert all(Path(a.path).exists() for a in artifacts)
    assert all(a.format == "png" for a in artifacts)
    assert all(Path(a.path).parent.name == "images" for a in artifacts)


def test_chart_artifacts_have_required_categories(tmp_path: Path) -> None:
    df = _build_chart_df()
    generate_standard_charts(df, output_dir=tmp_path, clean_output=True, write_png=True)

    listed = list_chart_artifacts(output_dir=tmp_path)
    categories = {item.category for item in listed}

    assert {"overview", "correlation", "distribution", "category"}.issubset(categories)
    assert len(listed) >= 8
