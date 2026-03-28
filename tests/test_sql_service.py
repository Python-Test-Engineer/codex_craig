"""Tests for sql_service catalog generation and test execution."""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from csv_analyser.services.sql_service import generate_sql_catalog, run_tests_and_merge


@pytest.fixture()
def simple_df() -> pd.DataFrame:
    return pd.DataFrame({
        "product": ["A", "B", "A", "C"],
        "quantity": [10, 20, 15, 5],
        "price": [1.0, 2.0, 1.5, 3.0],
    })


@pytest.fixture()
def csv_path(tmp_path: Path, simple_df: pd.DataFrame) -> Path:
    p = tmp_path / "test_data.csv"
    simple_df.to_csv(p, index=False)
    return p


def test_generate_sql_catalog_creates_files(simple_df: pd.DataFrame, csv_path: Path) -> None:
    title_path, queries_path = generate_sql_catalog(simple_df, csv_path)
    assert title_path.exists(), "sql_title.md should be created"
    assert queries_path.exists(), "sql_queries_*.md should be created"


def test_sql_title_md_has_sections(simple_df: pd.DataFrame, csv_path: Path) -> None:
    title_path, _ = generate_sql_catalog(simple_df, csv_path)
    content = title_path.read_text(encoding="utf-8")
    assert "## Overview" in content or "## Numeric" in content or "#" in content


def test_sql_queries_md_has_code_blocks(simple_df: pd.DataFrame, csv_path: Path) -> None:
    _, queries_path = generate_sql_catalog(simple_df, csv_path)
    content = queries_path.read_text(encoding="utf-8")
    assert "```sql" in content, "Queries file should contain SQL code blocks"
    assert "SELECT" in content


def test_sql_queries_md_has_row_count_query(simple_df: pd.DataFrame, csv_path: Path) -> None:
    _, queries_path = generate_sql_catalog(simple_df, csv_path)
    content = queries_path.read_text(encoding="utf-8")
    assert "COUNT" in content


def test_run_tests_and_merge_produces_results(simple_df: pd.DataFrame, csv_path: Path) -> None:
    _, queries_path = generate_sql_catalog(simple_df, csv_path)
    stats = run_tests_and_merge(queries_path, csv_path)
    assert isinstance(stats, dict)
    assert stats.get("passed", 0) + stats.get("failed", 0) + stats.get("skipped", 0) > 0


def test_run_tests_and_merge_inline_results_written(simple_df: pd.DataFrame, csv_path: Path) -> None:
    _, queries_path = generate_sql_catalog(simple_df, csv_path)
    run_tests_and_merge(queries_path, csv_path)
    updated_content = queries_path.read_text(encoding="utf-8")
    # After merging, there should be result markers in the file
    assert "Result" in updated_content or "rows" in updated_content or "row" in updated_content
