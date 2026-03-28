"""Tests for dirty_service.find_dirty_rows."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from csv_analyser.services.dirty_service import find_dirty_rows


def _clean_df() -> pd.DataFrame:
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Carol"],
        "price": [10.0, 20.0, 30.0],
    })


def test_clean_dataset_has_no_dirty_rows() -> None:
    df = _clean_df()
    dirty_df, reasons = find_dirty_rows(df)
    assert len(dirty_df) == 0
    assert len(reasons) == 0


def test_missing_value_flagged() -> None:
    df = _clean_df()
    df.loc[1, "price"] = np.nan
    dirty_df, reasons = find_dirty_rows(df)
    assert 1 in reasons
    assert any("Missing" in r for r in reasons[1])


def test_exact_duplicate_flagged() -> None:
    df = pd.DataFrame({
        "name": ["Alice", "Alice"],
        "price": [10.0, 10.0],
    })
    dirty_df, reasons = find_dirty_rows(df)
    assert 1 in reasons
    assert any("duplicate" in r.lower() for r in reasons[1])
    # First occurrence should NOT be flagged
    assert 0 not in reasons


def test_outlier_flagged() -> None:
    # 19 normal values + 1 extreme outlier; with enough cluster points the
    # 3-sigma band excludes the extreme value even though the std is inflated.
    normal_values = [10.0] * 19
    df = pd.DataFrame({"score": normal_values + [1000.0]})
    dirty_df, reasons = find_dirty_rows(df)
    assert 19 in reasons
    assert any("Outlier" in r for r in reasons[19])


def test_negative_in_non_negative_column_flagged() -> None:
    df = pd.DataFrame({"price": [10.0, -5.0, 20.0]})
    dirty_df, reasons = find_dirty_rows(df)
    assert 1 in reasons
    assert any("Negative" in r for r in reasons[1])


def test_negative_in_neutral_column_not_flagged() -> None:
    df = pd.DataFrame({"temperature": [20.0, -5.0, 15.0]})
    _, reasons = find_dirty_rows(df)
    # -5 is not an outlier (within 3 std), and 'temperature' is not in non-negative hints
    # So index 1 should not have a negative-value reason
    neg_flagged = any("Negative" in r for r in reasons.get(1, []))
    assert not neg_flagged


@pytest.mark.parametrize("col,hint", [
    ("price", True),
    ("quantity", True),
    ("revenue", True),
    ("score", True),
    ("temperature", False),
    ("id", False),
])
def test_non_negative_hints(col: str, hint: bool) -> None:
    from csv_analyser.services.dirty_service import _should_be_non_negative
    assert _should_be_non_negative(col) == hint
