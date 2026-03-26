# SQL Test Results

Queries file: `output\sql\sql_queries_data.md`  
Source CSV: `data\data.csv` (in-memory SQLite)  
Queries run: **24** (all)

---

**Summary:** 21 passed · 0 failed · 3 skipped

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
| 20 |

---

## 2. Column Sample

**Status:** OK

```sql
SELECT *
FROM data
LIMIT 10;
```

**Rows returned:** 10

| order_id | date | product_name | unit_price | quantity | total_price | city |
| --- | --- | --- | --- | --- | --- | --- |
| ORD0001 | 2025-04-28 | Monitor | 349.99 | 10 | 3499.9 | New York |
| ORD0002 | 2025-09-29 | Mouse | 29.99 | 5 | 149.95 | New York |
| ORD0003 | 2025-08-04 | Headphones | 149.99 | 8 | 1199.92 | Chicago |
| ORD0004 | 2025-12-16 | Headphones | 149.99 | 6 | 899.94 | New York |
| ORD0005 | 2025-02-12 | Mouse | 29.99 | 3 | 89.97 | Los Angeles |
| ORD0008 | 2025-11-07 | Headphones | 149.99 | 9 | 1349.91 | Los Angeles |
| ORD0009 | 2025-03-24 | Monitor | 349.99 | 3 | 1049.97 | Los Angeles |
| ORD0011 | 2025-02-11 | Laptop | 999.99 | 8 | 7999.92 | New York |
| ORD0012 | 2025-07-15 | Monitor | 349.99 | 5 | 1749.95 | New York |
| ORD0013 | 2025-01-29 | Keyboard | 79.99 | 7 | 559.93 | Chicago |

---

## 3. Summary Stats for unit_price

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
| 29.99 | 999.99 | 403.49 | 8069.8 |

---

## 4. Summary Stats for quantity

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
| 3 | 10 | 6.65 | 133 |

---

## 5. Summary Stats for total_price

**Status:** OK

```sql
SELECT
    MIN(total_price) AS min_val,
    MAX(total_price) AS max_val,
    ROUND(AVG(total_price), 2) AS avg_val,
    SUM(total_price) AS total
FROM data;
```

**Rows returned:** 1

| min_val | max_val | avg_val | total |
| --- | --- | --- | --- |
| 89.97 | 7999.92 | 2695.93 | 53918.67 |

---

## 6. Total unit_price by product_name

**Status:** OK

```sql
SELECT product_name, SUM(unit_price) AS total_unit_price
FROM data
GROUP BY product_name
ORDER BY total_unit_price DESC;
```

**Rows returned:** 5

| product_name | total_unit_price |
| --- | --- |
| Laptop | 4999.95 |
| Monitor | 2099.94 |
| Headphones | 749.95 |
| Keyboard | 159.98 |
| Mouse | 59.98 |

---

## 7. Average unit_price by product_name

**Status:** OK

```sql
SELECT product_name, ROUND(AVG(unit_price), 2) AS avg_unit_price
FROM data
GROUP BY product_name
ORDER BY avg_unit_price DESC;
```

**Rows returned:** 5

| product_name | avg_unit_price |
| --- | --- |
| Laptop | 999.99 |
| Monitor | 349.99 |
| Headphones | 149.99 |
| Keyboard | 79.99 |
| Mouse | 29.99 |

---

## 8. Total quantity by product_name

**Status:** OK

```sql
SELECT product_name, SUM(quantity) AS total_quantity
FROM data
GROUP BY product_name
ORDER BY total_quantity DESC;
```

**Rows returned:** 5

| product_name | total_quantity |
| --- | --- |
| Monitor | 40 |
| Headphones | 36 |
| Laptop | 33 |
| Keyboard | 16 |
| Mouse | 8 |

---

## 9. Distribution of product_name

**Status:** OK

```sql
SELECT product_name, COUNT(*) AS row_count
FROM data
GROUP BY product_name
ORDER BY row_count DESC;
```

**Rows returned:** 5

| product_name | row_count |
| --- | --- |
| Monitor | 6 |
| Laptop | 5 |
| Headphones | 5 |
| Mouse | 2 |
| Keyboard | 2 |

---

## 10. Distribution of city

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
| Los Angeles | 8 |
| New York | 7 |
| Chicago | 5 |

---

## 11. Top 10 product_name by unit_price

**Status:** OK

```sql
SELECT product_name, SUM(unit_price) AS total_unit_price
FROM data
GROUP BY product_name
ORDER BY total_unit_price DESC
LIMIT 10;
```

**Rows returned:** 5

| product_name | total_unit_price |
| --- | --- |
| Laptop | 4999.95 |
| Monitor | 2099.94 |
| Headphones | 749.95 |
| Keyboard | 159.98 |
| Mouse | 59.98 |

---

## 12. Bottom 10 product_name by unit_price

**Status:** OK

```sql
SELECT product_name, SUM(unit_price) AS total_unit_price
FROM data
GROUP BY product_name
ORDER BY total_unit_price ASC
LIMIT 10;
```

**Rows returned:** 5

| product_name | total_unit_price |
| --- | --- |
| Mouse | 59.98 |
| Keyboard | 159.98 |
| Headphones | 749.95 |
| Monitor | 2099.94 |
| Laptop | 4999.95 |

---

## 13. Top 10 city by unit_price

**Status:** OK

```sql
SELECT city, SUM(unit_price) AS total_unit_price
FROM data
GROUP BY city
ORDER BY total_unit_price DESC
LIMIT 10;
```

**Rows returned:** 3

| city | total_unit_price |
| --- | --- |
| New York | 2959.93 |
| Los Angeles | 2729.92 |
| Chicago | 2379.95 |

---

## 14. unit_price by product_name and city

**Status:** OK

```sql
SELECT product_name, city, SUM(unit_price) AS total_unit_price
FROM data
GROUP BY product_name, city
ORDER BY total_unit_price DESC;
```

**Rows returned:** 12

| product_name | city | total_unit_price |
| --- | --- | --- |
| Laptop | Chicago | 1999.98 |
| Laptop | New York | 1999.98 |
| Monitor | Los Angeles | 1399.96 |
| Laptop | Los Angeles | 999.99 |
| Monitor | New York | 699.98 |
| Headphones | Chicago | 299.98 |
| Headphones | Los Angeles | 299.98 |
| Headphones | New York | 149.99 |
| Keyboard | Chicago | 79.99 |
| Keyboard | New York | 79.99 |
| Mouse | Los Angeles | 29.99 |
| Mouse | New York | 29.99 |

---

## 15. Filter by product_name

**Status:** SKIPPED

```sql
SELECT *
FROM data
WHERE product_name = :product_name;
```

**Skipped:** Query requires runtime arguments (:param)

---

## 16. Total unit_price for a Specific product_name

**Status:** SKIPPED

```sql
SELECT product_name, SUM(unit_price) AS total_unit_price
FROM data
WHERE product_name = :product_name
GROUP BY product_name;
```

**Skipped:** Query requires runtime arguments (:param)

---

## 17. Monthly unit_price Trend

**Status:** OK

```sql
SELECT
    strftime('%Y-%m', date) AS month,
    SUM(unit_price) AS total_unit_price
FROM data
GROUP BY month
ORDER BY month;
```

**Rows returned:** 11

| month | total_unit_price |
| --- | --- |
| 2025-01 | 429.98 |
| 2025-02 | 1379.97 |
| 2025-03 | 1429.97 |
| 2025-04 | 1849.96 |
| 2025-06 | 999.99 |
| 2025-07 | 349.99 |
| 2025-08 | 149.99 |
| 2025-09 | 1029.98 |
| 2025-10 | 149.99 |
| 2025-11 | 149.99 |
| 2025-12 | 149.99 |

---

## 18. Yearly unit_price Total

**Status:** OK

```sql
SELECT
    strftime('%Y', date) AS year,
    SUM(unit_price) AS total_unit_price
FROM data
GROUP BY year
ORDER BY year;
```

**Rows returned:** 1

| year | total_unit_price |
| --- | --- |
| 2025 | 8069.8 |

---

## 19. Date Range Filter

**Status:** SKIPPED

```sql
SELECT *
FROM data
WHERE date BETWEEN :start_date AND :end_date
ORDER BY date;
```

**Skipped:** Query requires runtime arguments (:param)

---

## 20. Missing Values per Column

**Status:** OK

```sql
SELECT 'order_id' AS column_name, COUNT(*) AS null_count FROM data WHERE order_id IS NULL
UNION ALL
SELECT 'date' AS column_name, COUNT(*) AS null_count FROM data WHERE date IS NULL
UNION ALL
SELECT 'product_name' AS column_name, COUNT(*) AS null_count FROM data WHERE product_name IS NULL
UNION ALL
SELECT 'unit_price' AS column_name, COUNT(*) AS null_count FROM data WHERE unit_price IS NULL
UNION ALL
SELECT 'quantity' AS column_name, COUNT(*) AS null_count FROM data WHERE quantity IS NULL
UNION ALL
SELECT 'total_price' AS column_name, COUNT(*) AS null_count FROM data WHERE total_price IS NULL
UNION ALL
SELECT 'city' AS column_name, COUNT(*) AS null_count FROM data WHERE city IS NULL
ORDER BY null_count DESC;
```

**Rows returned:** 7

| column_name | null_count |
| --- | --- |
| order_id | 0 |
| date | 0 |
| product_name | 0 |
| unit_price | 0 |
| quantity | 0 |
| total_price | 0 |
| city | 0 |

---

## 21. Duplicate order_id Values

**Status:** OK

```sql
SELECT order_id, COUNT(*) AS occurrences
FROM data
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;
```

**Rows returned:** 0

*(no rows returned)*

---

## 22. Negative unit_price Values

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

## 23. Negative quantity Values

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

## 24. Negative total_price Values

**Status:** OK

```sql
SELECT *
FROM data
WHERE total_price < 0
ORDER BY total_price;
```

**Rows returned:** 0

*(no rows returned)*

---
