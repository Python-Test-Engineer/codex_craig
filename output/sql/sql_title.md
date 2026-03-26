# SQL Query Catalog — data.csv

Dataset: `data\data.csv`
Columns: `order_id`, `date`, `customer_id`, `customer_name`, `product_id`, `product_name`, `unit_cost`, `unit_price`, `quantity`, `total_cost`, `total_revenue`, `profit`, `margin_pct`, `store_id`, `store_name`, `city`, `payment_method`

---

## Overview

1. Row Count — Returns the total number of rows in the dataset.
2. Column Sample — Returns the first 10 rows to preview the dataset structure.

---

## Numeric Summaries

3. Summary Stats for unit_cost — Returns min, max, average, and total for unit_cost.
4. Summary Stats for unit_price — Returns min, max, average, and total for unit_price.
5. Summary Stats for quantity — Returns min, max, average, and total for quantity.
6. Summary Stats for total_cost — Returns min, max, average, and total for total_cost.
7. Summary Stats for total_revenue — Returns min, max, average, and total for total_revenue.
8. Summary Stats for profit — Returns min, max, average, and total for profit.
9. Total unit_cost by date — Ranks each date by total unit_cost, highest first.
10. Average unit_cost by date — Compares average unit_cost across each date.
11. Total unit_price by date — Ranks each date by total unit_price, highest first.

---

## Categorical Distributions

12. Distribution of date — Counts rows for each distinct value of date, ordered by frequency.
13. Distribution of customer_name — Counts rows for each distinct value of customer_name, ordered by frequency.
14. Distribution of product_name — Counts rows for each distinct value of product_name, ordered by frequency.
15. Distribution of store_name — Counts rows for each distinct value of store_name, ordered by frequency.
16. Distribution of city — Counts rows for each distinct value of city, ordered by frequency.

---

## Rankings

17. Top 10 date by unit_cost — Lists the 10 date values with the highest total unit_cost.
18. Bottom 10 date by unit_cost — Lists the 10 date values with the lowest total unit_cost.
19. Top 10 customer_name by unit_cost — Lists the 10 customer_name values with the highest total unit_cost.

---

## Multi-Dimensional

20. unit_cost by date and customer_name — Shows total unit_cost broken down by both date and customer_name.

---

## Parametric Lookups

21. Filter by date — Returns all rows where date matches a given value.
22. Total unit_cost for a Specific date — Returns total unit_cost for a single date value.

---

## Data Quality Checks

23. Missing Values per Column — Counts NULL values in each column to identify data gaps.
24. Duplicate order_id Values — Flags any order_id that appears more than once in the dataset.
25. Negative unit_cost Values — Flags rows where unit_cost is negative, which may indicate data errors.
26. Negative unit_price Values — Flags rows where unit_price is negative, which may indicate data errors.
27. Negative quantity Values — Flags rows where quantity is negative, which may indicate data errors.

---

*Generated from dataset inspection — data.csv (39 rows, 17 columns)*