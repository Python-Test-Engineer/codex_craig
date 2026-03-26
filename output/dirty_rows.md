# Dirty Row Report

- **Total rows in dataset:** 39
- **Dirty rows identified:** 1
- **Clean rows:** 38

## Criteria Used

A row is flagged as **dirty** if it satisfies one or more of the following conditions:

| # | Criterion | Description |
|---|-----------|-------------|
| 1 | **Missing value** | One or more cells are null / NaN |
| 2 | **Exact duplicate** | Row is an identical copy of an earlier row |
| 3 | **Numeric outlier** | A numeric value falls outside +/- 3 standard deviations from the column mean |
| 4 | **Negative in non-negative column** | A numeric value is negative in a column whose name implies non-negative values (price, quantity, total, etc.) |

## Summary by Criterion

- **Exact duplicates:** 1 row(s)

## Row-by-Row Detail

### Row 38
- Exact duplicate of a previous row

