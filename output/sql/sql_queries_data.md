# SQL Query Catalog
<!-- source: data.csv | table: data | generated: 2026-03-26 | queries: 27 -->

---

### Overview

## Row Count
**ARGS:** —
**Description:** Returns the total number of rows in the dataset.
```sql
SELECT COUNT(*) AS row_count
FROM data;
```

**Status:** OK

**Rows returned:** 1

| row_count |
| --- |
| 39 |
---

## Column Sample
**ARGS:** —
**Description:** Returns the first 10 rows to preview the dataset structure.
```sql
SELECT *
FROM data
LIMIT 10;
```

**Status:** OK

**Rows returned:** 10

| order_id | date | customer_id | customer_name | product_id | product_name | unit_cost | unit_price | quantity | total_cost | total_revenue | profit | margin_pct | store_id | store_name | city | payment_method |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ORD0001 | 2025-02-28 | C06 | Frank Miller | P003 | Keyboard | 28.0 | 79.99 | 4 | 112.0 | 319.96 | 207.96 | 65.0 | S1 | Store Alpha | New York | Debit Card |
| ORD0002 | 2025-03-16 | C08 | Henry Moore | P003 | Keyboard | 28.0 | 79.99 | 10 | 280.0 | 799.9 | 519.9 | 65.0 | S3 | Store Gamma | Chicago | Debit Card |
| ORD0003 | 2025-09-12 | C09 | Isabella Taylor | P005 | Headphones | 55.0 | 149.99 | 5 | 275.0 | 749.95 | 474.95 | 63.3 | S1 | Store Alpha | New York | Credit Card |
| ORD0004 | 2025-06-19 | C04 | David Brown | P002 | Mouse | 8.5 | 29.99 | 7 | 59.5 | 209.93 | 150.43 | 71.7 | S3 | Store Gamma | Chicago | Debit Card |
| ORD0005 | 2025-10-01 | C02 | Bob Smith | P003 | Keyboard | 28.0 | 79.99 | 9 | 252.0 | 719.91 | 467.91 | 65.0 | S1 | Store Alpha | New York | Cash |
| ORD0006 | 2025-02-11 | C04 | David Brown | P004 | Monitor | 180.0 | 349.99 | 4 | 720.0 | 1399.96 | 679.96 | 48.6 | S1 | Store Alpha | New York | Credit Card |
| ORD0007 | 2025-02-21 | C09 | Isabella Taylor | P002 | Mouse | 8.5 | 29.99 | 10 | 85.0 | 299.9 | 214.9 | 71.7 | S2 | Store Beta | Los Angeles | Credit Card |
| ORD0008 | 2025-02-10 | C06 | Frank Miller | P002 | Mouse | 8.5 | 29.99 | 2 | 17.0 | 59.98 | 42.98 | 71.7 | S1 | Store Alpha | New York | PayPal |
| ORD0009 | 2025-06-29 | C02 | Bob Smith | P005 | Headphones | 55.0 | 149.99 | 8 | 440.0 | 1199.92 | 759.92 | 63.3 | S2 | Store Beta | Los Angeles | Credit Card |
| ORD0039 | 2025-06-16 | C04 | David Brown | P004 | Monitor | 180.0 | 349.99 | 10 | 1800.0 | 3499.9 | 1699.9 | 48.6 | S3 | Store Gamma | Chicago | Cash |
---

### Numeric Summaries

## Summary Stats for unit_cost
**ARGS:** —
**Description:** Returns min, max, average, and total for unit_cost.
```sql
SELECT
    MIN(unit_cost) AS min_val,
    MAX(unit_cost) AS max_val,
    ROUND(AVG(unit_cost), 2) AS avg_val,
    SUM(unit_cost) AS total
FROM data;
```

**Status:** OK

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 8.5 | 650.0 | 198.42 | 7738.5 |
---

## Summary Stats for unit_price
**ARGS:** —
**Description:** Returns min, max, average, and total for unit_price.
```sql
SELECT
    MIN(unit_price) AS min_val,
    MAX(unit_price) AS max_val,
    ROUND(AVG(unit_price), 2) AS avg_val,
    SUM(unit_price) AS total
FROM data;
```

**Status:** OK

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 29.99 | 999.99 | 344.86 | 13449.61 |
---

## Summary Stats for quantity
**ARGS:** —
**Description:** Returns min, max, average, and total for quantity.
```sql
SELECT
    MIN(quantity) AS min_val,
    MAX(quantity) AS max_val,
    ROUND(AVG(quantity), 2) AS avg_val,
    SUM(quantity) AS total
FROM data;
```

**Status:** OK

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 1 | 10 | 6.05 | 236 |
---

## Summary Stats for total_cost
**ARGS:** —
**Description:** Returns min, max, average, and total for total_cost.
```sql
SELECT
    MIN(total_cost) AS min_val,
    MAX(total_cost) AS max_val,
    ROUND(AVG(total_cost), 2) AS avg_val,
    SUM(total_cost) AS total
FROM data;
```

**Status:** OK

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 17.0 | 6500.0 | 1206.41 | 47050.0 |
---

## Summary Stats for total_revenue
**ARGS:** —
**Description:** Returns min, max, average, and total for total_revenue.
```sql
SELECT
    MIN(total_revenue) AS min_val,
    MAX(total_revenue) AS max_val,
    ROUND(AVG(total_revenue), 2) AS avg_val,
    SUM(total_revenue) AS total
FROM data;
```

**Status:** OK

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 59.98 | 9999.9 | 2096.09 | 81747.64 |
---

## Summary Stats for profit
**ARGS:** —
**Description:** Returns min, max, average, and total for profit.
```sql
SELECT
    MIN(profit) AS min_val,
    MAX(profit) AS max_val,
    ROUND(AVG(profit), 2) AS avg_val,
    SUM(profit) AS total
FROM data;
```

**Status:** OK

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 42.98 | 3499.9 | 889.68 | 34697.64 |
---

## Total unit_cost by date
**ARGS:** —
**Description:** Ranks each date by total unit_cost, highest first.
```sql
SELECT date, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY date
ORDER BY total_unit_cost DESC;
```

**Status:** OK

**Rows returned:** 37

| date | total_unit_cost |
| --- | --- |
| 2025-10-04 | 650.0 |
| 2025-09-28 | 650.0 |
| 2025-08-10 | 650.0 |
| 2025-08-06 | 650.0 |
| 2025-04-02 | 650.0 |
| 2025-03-24 | 650.0 |
| 2025-01-29 | 650.0 |
| 2025-01-20 | 650.0 |
| 2025-06-16 | 360.0 |
| 2025-11-29 | 180.0 |
| 2025-08-09 | 180.0 |
| 2025-06-11 | 180.0 |
| 2025-03-11 | 180.0 |
| 2025-02-15 | 180.0 |
| 2025-02-11 | 180.0 |
| 2025-02-01 | 180.0 |
| 2025-01-09 | 180.0 |
| 2025-01-05 | 180.0 |
| 2025-02-10 | 63.5 |
| 2025-11-03 | 55.0 |

*…17 more rows not shown*
---

## Average unit_cost by date
**ARGS:** —
**Description:** Compares average unit_cost across each date.
```sql
SELECT date, ROUND(AVG(unit_cost), 2) AS avg_unit_cost
FROM data
GROUP BY date
ORDER BY avg_unit_cost DESC;
```

**Status:** OK

**Rows returned:** 37

| date | avg_unit_cost |
| --- | --- |
| 2025-10-04 | 650.0 |
| 2025-09-28 | 650.0 |
| 2025-08-10 | 650.0 |
| 2025-08-06 | 650.0 |
| 2025-04-02 | 650.0 |
| 2025-03-24 | 650.0 |
| 2025-01-29 | 650.0 |
| 2025-01-20 | 650.0 |
| 2025-11-29 | 180.0 |
| 2025-08-09 | 180.0 |
| 2025-06-16 | 180.0 |
| 2025-06-11 | 180.0 |
| 2025-03-11 | 180.0 |
| 2025-02-15 | 180.0 |
| 2025-02-11 | 180.0 |
| 2025-02-01 | 180.0 |
| 2025-01-09 | 180.0 |
| 2025-01-05 | 180.0 |
| 2025-11-03 | 55.0 |
| 2025-09-12 | 55.0 |

*…17 more rows not shown*
---

## Total unit_price by date
**ARGS:** —
**Description:** Ranks each date by total unit_price, highest first.
```sql
SELECT date, SUM(unit_price) AS total_unit_price
FROM data
GROUP BY date
ORDER BY total_unit_price DESC;
```

**Status:** OK

**Rows returned:** 37

| date | total_unit_price |
| --- | --- |
| 2025-10-04 | 999.99 |
| 2025-09-28 | 999.99 |
| 2025-08-10 | 999.99 |
| 2025-08-06 | 999.99 |
| 2025-04-02 | 999.99 |
| 2025-03-24 | 999.99 |
| 2025-01-29 | 999.99 |
| 2025-01-20 | 999.99 |
| 2025-06-16 | 699.98 |
| 2025-11-29 | 349.99 |
| 2025-08-09 | 349.99 |
| 2025-06-11 | 349.99 |
| 2025-03-11 | 349.99 |
| 2025-02-15 | 349.99 |
| 2025-02-11 | 349.99 |
| 2025-02-01 | 349.99 |
| 2025-01-09 | 349.99 |
| 2025-01-05 | 349.99 |
| 2025-02-10 | 179.98000000000002 |
| 2025-11-03 | 149.99 |

*…17 more rows not shown*
---

### Categorical Distributions

## Distribution of date
**ARGS:** —
**Description:** Counts rows for each distinct value of date, ordered by frequency.
```sql
SELECT date, COUNT(*) AS row_count
FROM data
GROUP BY date
ORDER BY row_count DESC;
```

**Status:** OK

**Rows returned:** 37

| date | row_count |
| --- | --- |
| 2025-06-16 | 2 |
| 2025-02-10 | 2 |
| 2025-12-23 | 1 |
| 2025-11-29 | 1 |
| 2025-11-03 | 1 |
| 2025-10-31 | 1 |
| 2025-10-23 | 1 |
| 2025-10-04 | 1 |
| 2025-10-01 | 1 |
| 2025-09-28 | 1 |
| 2025-09-16 | 1 |
| 2025-09-12 | 1 |
| 2025-08-24 | 1 |
| 2025-08-10 | 1 |
| 2025-08-09 | 1 |
| 2025-08-06 | 1 |
| 2025-06-29 | 1 |
| 2025-06-19 | 1 |
| 2025-06-11 | 1 |
| 2025-04-02 | 1 |

*…17 more rows not shown*
---

## Distribution of customer_name
**ARGS:** —
**Description:** Counts rows for each distinct value of customer_name, ordered by frequency.
```sql
SELECT customer_name, COUNT(*) AS row_count
FROM data
GROUP BY customer_name
ORDER BY row_count DESC;
```

**Status:** OK

**Rows returned:** 10

| customer_name | row_count |
| --- | --- |
| Bob Smith | 10 |
| Emma Davis | 5 |
| David Brown | 5 |
| Isabella Taylor | 4 |
| Henry Moore | 3 |
| Frank Miller | 3 |
| Alice Johnson | 3 |
| Jack Anderson | 2 |
| Grace Wilson | 2 |
| Carol White | 2 |
---

## Distribution of product_name
**ARGS:** —
**Description:** Counts rows for each distinct value of product_name, ordered by frequency.
```sql
SELECT product_name, COUNT(*) AS row_count
FROM data
GROUP BY product_name
ORDER BY row_count DESC;
```

**Status:** OK

**Rows returned:** 6

| product_name | row_count |
| --- | --- |
| Monitor | 11 |
| Laptop | 8 |
| Keyboard | 8 |
| Mouse | 6 |
| Headphones | 5 |
| Mousse | 1 |
---

## Distribution of store_name
**ARGS:** —
**Description:** Counts rows for each distinct value of store_name, ordered by frequency.
```sql
SELECT store_name, COUNT(*) AS row_count
FROM data
GROUP BY store_name
ORDER BY row_count DESC;
```

**Status:** OK

**Rows returned:** 3

| store_name | row_count |
| --- | --- |
| Store Beta | 14 |
| Store Alpha | 13 |
| Store Gamma | 12 |
---

## Distribution of city
**ARGS:** —
**Description:** Counts rows for each distinct value of city, ordered by frequency.
```sql
SELECT city, COUNT(*) AS row_count
FROM data
GROUP BY city
ORDER BY row_count DESC;
```

**Status:** OK

**Rows returned:** 3

| city | row_count |
| --- | --- |
| Los Angeles | 14 |
| New York | 13 |
| Chicago | 12 |
---

### Rankings

## Top 10 date by unit_cost
**ARGS:** —
**Description:** Lists the 10 date values with the highest total unit_cost.
```sql
SELECT date, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY date
ORDER BY total_unit_cost DESC
LIMIT 10;
```

**Status:** OK

**Rows returned:** 10

| date | total_unit_cost |
| --- | --- |
| 2025-10-04 | 650.0 |
| 2025-09-28 | 650.0 |
| 2025-08-10 | 650.0 |
| 2025-08-06 | 650.0 |
| 2025-04-02 | 650.0 |
| 2025-03-24 | 650.0 |
| 2025-01-29 | 650.0 |
| 2025-01-20 | 650.0 |
| 2025-06-16 | 360.0 |
| 2025-11-29 | 180.0 |
---

## Bottom 10 date by unit_cost
**ARGS:** —
**Description:** Lists the 10 date values with the lowest total unit_cost.
```sql
SELECT date, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY date
ORDER BY total_unit_cost ASC
LIMIT 10;
```

**Status:** OK

**Rows returned:** 10

| date | total_unit_cost |
| --- | --- |
| 2025-02-21 | 8.5 |
| 2025-03-26 | 8.5 |
| 2025-06-19 | 8.5 |
| 2025-08-24 | 8.5 |
| 2025-09-16 | 8.5 |
| 2025-10-23 | 8.5 |
| 2025-01-25 | 28.0 |
| 2025-02-05 | 28.0 |
| 2025-02-14 | 28.0 |
| 2025-02-28 | 28.0 |
---

## Top 10 customer_name by unit_cost
**ARGS:** —
**Description:** Lists the 10 customer_name values with the highest total unit_cost.
```sql
SELECT customer_name, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY customer_name
ORDER BY total_unit_cost DESC
LIMIT 10;
```

**Status:** OK

**Rows returned:** 10

| customer_name | total_unit_cost |
| --- | --- |
| Bob Smith | 1987.5 |
| David Brown | 1198.5 |
| Isabella Taylor | 893.5 |
| Emma Davis | 875.0 |
| Henry Moore | 733.0 |
| Alice Johnson | 686.5 |
| Jack Anderson | 678.0 |
| Carol White | 360.0 |
| Frank Miller | 216.5 |
| Grace Wilson | 110.0 |
---

### Multi-Dimensional

## unit_cost by date and customer_name
**ARGS:** —
**Description:** Shows total unit_cost broken down by both date and customer_name.
```sql
SELECT date, customer_name, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY date, customer_name
ORDER BY total_unit_cost DESC;
```

**Status:** OK

**Rows returned:** 38

| date | customer_name | total_unit_cost |
| --- | --- | --- |
| 2025-01-20 | Bob Smith | 650.0 |
| 2025-01-29 | Emma Davis | 650.0 |
| 2025-03-24 | Jack Anderson | 650.0 |
| 2025-04-02 | Isabella Taylor | 650.0 |
| 2025-08-06 | Bob Smith | 650.0 |
| 2025-08-10 | Alice Johnson | 650.0 |
| 2025-09-28 | David Brown | 650.0 |
| 2025-10-04 | Henry Moore | 650.0 |
| 2025-06-16 | David Brown | 360.0 |
| 2025-01-05 | Bob Smith | 180.0 |
| 2025-01-09 | Bob Smith | 180.0 |
| 2025-02-01 | Frank Miller | 180.0 |
| 2025-02-11 | David Brown | 180.0 |
| 2025-02-15 | Carol White | 180.0 |
| 2025-03-11 | Bob Smith | 180.0 |
| 2025-06-11 | Emma Davis | 180.0 |
| 2025-08-09 | Carol White | 180.0 |
| 2025-11-29 | Isabella Taylor | 180.0 |
| 2025-01-07 | Henry Moore | 55.0 |
| 2025-02-10 | Grace Wilson | 55.0 |

*…18 more rows not shown*
---

### Parametric Lookups

## Filter by date
**ARGS:** date
**Description:** Returns all rows where date matches a given value.
```sql
SELECT *
FROM data
WHERE date = :date;
```

**Status:** SKIPPED

**Skipped:** Query requires runtime arguments (:param)
---

## Total unit_cost for a Specific date
**ARGS:** date
**Description:** Returns total unit_cost for a single date value.
```sql
SELECT date, SUM(unit_cost) AS total_unit_cost
FROM data
WHERE date = :date
GROUP BY date;
```

**Status:** SKIPPED

**Skipped:** Query requires runtime arguments (:param)
---

### Data Quality Checks

## Missing Values per Column
**ARGS:** —
**Description:** Counts NULL values in each column to identify data gaps.
```sql
SELECT 'order_id' AS column_name, COUNT(*) AS null_count FROM data WHERE order_id IS NULL
UNION ALL
SELECT 'date' AS column_name, COUNT(*) AS null_count FROM data WHERE date IS NULL
UNION ALL
SELECT 'customer_id' AS column_name, COUNT(*) AS null_count FROM data WHERE customer_id IS NULL
UNION ALL
SELECT 'customer_name' AS column_name, COUNT(*) AS null_count FROM data WHERE customer_name IS NULL
UNION ALL
SELECT 'product_id' AS column_name, COUNT(*) AS null_count FROM data WHERE product_id IS NULL
UNION ALL
SELECT 'product_name' AS column_name, COUNT(*) AS null_count FROM data WHERE product_name IS NULL
UNION ALL
SELECT 'unit_cost' AS column_name, COUNT(*) AS null_count FROM data WHERE unit_cost IS NULL
UNION ALL
SELECT 'unit_price' AS column_name, COUNT(*) AS null_count FROM data WHERE unit_price IS NULL
UNION ALL
SELECT 'quantity' AS column_name, COUNT(*) AS null_count FROM data WHERE quantity IS NULL
UNION ALL
SELECT 'total_cost' AS column_name, COUNT(*) AS null_count FROM data WHERE total_cost IS NULL
UNION ALL
SELECT 'total_revenue' AS column_name, COUNT(*) AS null_count FROM data WHERE total_revenue IS NULL
UNION ALL
SELECT 'profit' AS column_name, COUNT(*) AS null_count FROM data WHERE profit IS NULL
ORDER BY null_count DESC;
```

**Status:** OK

**Rows returned:** 12

| column_name | null_count |
| --- | --- |
| order_id | 0 |
| date | 0 |
| customer_id | 0 |
| customer_name | 0 |
| product_id | 0 |
| product_name | 0 |
| unit_cost | 0 |
| unit_price | 0 |
| quantity | 0 |
| total_cost | 0 |
| total_revenue | 0 |
| profit | 0 |
---

## Duplicate order_id Values
**ARGS:** —
**Description:** Flags any order_id that appears more than once in the dataset.
```sql
SELECT order_id, COUNT(*) AS occurrences
FROM data
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;
```

**Status:** OK

**Rows returned:** 1

| order_id | occurrences |
| --- | --- |
| ORD0039 | 2 |
---

## Negative unit_cost Values
**ARGS:** —
**Description:** Flags rows where unit_cost is negative, which may indicate data errors.
```sql
SELECT *
FROM data
WHERE unit_cost < 0
ORDER BY unit_cost;
```

**Status:** OK

**Rows returned:** 0

*(no rows returned)*
---

## Negative unit_price Values
**ARGS:** —
**Description:** Flags rows where unit_price is negative, which may indicate data errors.
```sql
SELECT *
FROM data
WHERE unit_price < 0
ORDER BY unit_price;
```

**Status:** OK

**Rows returned:** 0

*(no rows returned)*
---

## Negative quantity Values
**ARGS:** —
**Description:** Flags rows where quantity is negative, which may indicate data errors.
```sql
SELECT *
FROM data
WHERE quantity < 0
ORDER BY quantity;
```

**Status:** OK

**Rows returned:** 0

*(no rows returned)*
---