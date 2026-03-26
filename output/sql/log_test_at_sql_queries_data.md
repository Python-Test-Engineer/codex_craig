# SQL Test Results

Queries file: `C:\Users\mrcra\Desktop\data-intelligence-agent\output\sql\sql_queries_data.md`  
Source CSV: `data\data.csv` (in-memory SQLite)  
Queries run: **27** (all)

---

**Summary:** 25 passed · 0 failed · 2 skipped

---

## 1. Row Count

**Status:** OK

```sql
SELECT COUNT(*) AS row_count
FROM data;
```

**Rows returned:** 1

| row_count |
| --- |
| 39 |

---

## 2. Column Sample

**Status:** OK

```sql
SELECT *
FROM data
LIMIT 10;
```

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

## 3. Summary Stats for unit_cost

**Status:** OK

```sql
SELECT
    MIN(unit_cost) AS min_val,
    MAX(unit_cost) AS max_val,
    ROUND(AVG(unit_cost), 2) AS avg_val,
    SUM(unit_cost) AS total
FROM data;
```

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 8.5 | 650.0 | 198.42 | 7738.5 |

---

## 4. Summary Stats for unit_price

**Status:** OK

```sql
SELECT
    MIN(unit_price) AS min_val,
    MAX(unit_price) AS max_val,
    ROUND(AVG(unit_price), 2) AS avg_val,
    SUM(unit_price) AS total
FROM data;
```

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 29.99 | 999.99 | 344.86 | 13449.61 |

---

## 5. Summary Stats for quantity

**Status:** OK

```sql
SELECT
    MIN(quantity) AS min_val,
    MAX(quantity) AS max_val,
    ROUND(AVG(quantity), 2) AS avg_val,
    SUM(quantity) AS total
FROM data;
```

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 1 | 10 | 6.05 | 236 |

---

## 6. Summary Stats for total_cost

**Status:** OK

```sql
SELECT
    MIN(total_cost) AS min_val,
    MAX(total_cost) AS max_val,
    ROUND(AVG(total_cost), 2) AS avg_val,
    SUM(total_cost) AS total
FROM data;
```

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 17.0 | 6500.0 | 1206.41 | 47050.0 |

---

## 7. Summary Stats for total_revenue

**Status:** OK

```sql
SELECT
    MIN(total_revenue) AS min_val,
    MAX(total_revenue) AS max_val,
    ROUND(AVG(total_revenue), 2) AS avg_val,
    SUM(total_revenue) AS total
FROM data;
```

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 59.98 | 9999.9 | 2096.09 | 81747.64 |

---

## 8. Summary Stats for profit

**Status:** OK

```sql
SELECT
    MIN(profit) AS min_val,
    MAX(profit) AS max_val,
    ROUND(AVG(profit), 2) AS avg_val,
    SUM(profit) AS total
FROM data;
```

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 42.98 | 3499.9 | 889.68 | 34697.64 |

---

## 9. Total unit_cost by date

**Status:** OK

```sql
SELECT date, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY date
ORDER BY total_unit_cost DESC;
```

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

## 10. Average unit_cost by date

**Status:** OK

```sql
SELECT date, ROUND(AVG(unit_cost), 2) AS avg_unit_cost
FROM data
GROUP BY date
ORDER BY avg_unit_cost DESC;
```

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

## 11. Total unit_price by date

**Status:** OK

```sql
SELECT date, SUM(unit_price) AS total_unit_price
FROM data
GROUP BY date
ORDER BY total_unit_price DESC;
```

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

## 12. Distribution of date

**Status:** OK

```sql
SELECT date, COUNT(*) AS row_count
FROM data
GROUP BY date
ORDER BY row_count DESC;
```

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

## 13. Distribution of customer_name

**Status:** OK

```sql
SELECT customer_name, COUNT(*) AS row_count
FROM data
GROUP BY customer_name
ORDER BY row_count DESC;
```

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

## 14. Distribution of product_name

**Status:** OK

```sql
SELECT product_name, COUNT(*) AS row_count
FROM data
GROUP BY product_name
ORDER BY row_count DESC;
```

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

## 15. Distribution of store_name

**Status:** OK

```sql
SELECT store_name, COUNT(*) AS row_count
FROM data
GROUP BY store_name
ORDER BY row_count DESC;
```

**Rows returned:** 3

| store_name | row_count |
| --- | --- |
| Store Beta | 14 |
| Store Alpha | 13 |
| Store Gamma | 12 |

---

## 16. Distribution of city

**Status:** OK

```sql
SELECT city, COUNT(*) AS row_count
FROM data
GROUP BY city
ORDER BY row_count DESC;
```

**Rows returned:** 3

| city | row_count |
| --- | --- |
| Los Angeles | 14 |
| New York | 13 |
| Chicago | 12 |

---

## 17. Top 10 date by unit_cost

**Status:** OK

```sql
SELECT date, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY date
ORDER BY total_unit_cost DESC
LIMIT 10;
```

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

## 18. Bottom 10 date by unit_cost

**Status:** OK

```sql
SELECT date, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY date
ORDER BY total_unit_cost ASC
LIMIT 10;
```

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

## 19. Top 10 customer_name by unit_cost

**Status:** OK

```sql
SELECT customer_name, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY customer_name
ORDER BY total_unit_cost DESC
LIMIT 10;
```

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

## 20. unit_cost by date and customer_name

**Status:** OK

```sql
SELECT date, customer_name, SUM(unit_cost) AS total_unit_cost
FROM data
GROUP BY date, customer_name
ORDER BY total_unit_cost DESC;
```

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

## 21. Filter by date

**Status:** SKIPPED

```sql
SELECT *
FROM data
WHERE date = :date;
```

**Skipped:** Query requires runtime arguments (:param)

---

## 22. Total unit_cost for a Specific date

**Status:** SKIPPED

```sql
SELECT date, SUM(unit_cost) AS total_unit_cost
FROM data
WHERE date = :date
GROUP BY date;
```

**Skipped:** Query requires runtime arguments (:param)

---

## 23. Missing Values per Column

**Status:** OK

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

## 24. Duplicate order_id Values

**Status:** OK

```sql
SELECT order_id, COUNT(*) AS occurrences
FROM data
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;
```

**Rows returned:** 1

| order_id | occurrences |
| --- | --- |
| ORD0039 | 2 |

---

## 25. Negative unit_cost Values

**Status:** OK

```sql
SELECT *
FROM data
WHERE unit_cost < 0
ORDER BY unit_cost;
```

**Rows returned:** 0

*(no rows returned)*

---

## 26. Negative unit_price Values

**Status:** OK

```sql
SELECT *
FROM data
WHERE unit_price < 0
ORDER BY unit_price;
```

**Rows returned:** 0

*(no rows returned)*

---

## 27. Negative quantity Values

**Status:** OK

```sql
SELECT *
FROM data
WHERE quantity < 0
ORDER BY quantity;
```

**Rows returned:** 0

*(no rows returned)*

---
