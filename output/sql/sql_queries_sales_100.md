# SQL Query Catalog
<!-- source: data/sales_data_100.csv | table: sales_data_100 | generated: 2026-03-25 | queries: 57 -->

---

### 1. Revenue & Sales

## Total Sales Revenue
**ARGS:** —
```sql
SELECT SUM(total_revenue) AS total_sales_revenue
FROM sales_data_100
```
---

## Total Revenue by Product
**ARGS:** —
```sql
SELECT product_name,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY product_name
ORDER BY total_revenue DESC
```
---

## Total Revenue by Store
**ARGS:** —
```sql
SELECT store_name,
       city,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY store_name, city
ORDER BY total_revenue DESC
```
---

## Total Revenue by City
**ARGS:** —
```sql
SELECT city,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY city
ORDER BY total_revenue DESC
```
---

## Total Revenue by Month
**ARGS:** —
```sql
SELECT STRFTIME('%Y-%m', date) AS month,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY month
ORDER BY month
```
---

## Total Revenue by Quarter
**ARGS:** —
```sql
SELECT STRFTIME('%Y', date) AS year,
       'Q' || CAST((CAST(STRFTIME('%m', date) AS INTEGER) - 1) / 3 + 1 AS TEXT) AS quarter,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY year, quarter
ORDER BY year, quarter
```
---

## Total Revenue by Customer
**ARGS:** —
```sql
SELECT customer_id,
       customer_name,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY customer_id, customer_name
ORDER BY total_revenue DESC
```
---

## Total Revenue by Payment Method
**ARGS:** —
```sql
SELECT payment_method,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY payment_method
ORDER BY total_revenue DESC
```
---

## Average Order Revenue
**ARGS:** —
```sql
SELECT ROUND(AVG(total_revenue), 2) AS avg_order_revenue
FROM sales_data_100
```
---

### 2. Volume & Orders

## Total Number of Orders
**ARGS:** —
```sql
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales_data_100
```
---

## Total Units Sold
**ARGS:** —
```sql
SELECT SUM(quantity) AS total_units_sold
FROM sales_data_100
```
---

## Total Units Sold by Product
**ARGS:** —
```sql
SELECT product_name,
       SUM(quantity) AS total_units_sold
FROM sales_data_100
GROUP BY product_name
ORDER BY total_units_sold DESC
```
---

## Total Units Sold by Store
**ARGS:** —
```sql
SELECT store_name,
       city,
       SUM(quantity) AS total_units_sold
FROM sales_data_100
GROUP BY store_name, city
ORDER BY total_units_sold DESC
```
---

## Total Orders by Customer
**ARGS:** —
```sql
SELECT customer_id,
       customer_name,
       COUNT(order_id) AS total_orders
FROM sales_data_100
GROUP BY customer_id, customer_name
ORDER BY total_orders DESC
```
---

## Average Units per Order
**ARGS:** —
```sql
SELECT ROUND(AVG(quantity), 2) AS avg_units_per_order
FROM sales_data_100
```
---

## Largest Orders by Quantity
**ARGS:** —
```sql
SELECT order_id,
       date,
       customer_name,
       product_name,
       quantity
FROM sales_data_100
ORDER BY quantity DESC
```
---

### 3. Profit & Margin

## Total Profit
**ARGS:** —
```sql
SELECT SUM(profit) AS total_profit
FROM sales_data_100
```
---

## Total Profit by Product
**ARGS:** —
```sql
SELECT product_name,
       SUM(profit) AS total_profit
FROM sales_data_100
GROUP BY product_name
ORDER BY total_profit DESC
```
---

## Total Profit by Store
**ARGS:** —
```sql
SELECT store_name,
       city,
       SUM(profit) AS total_profit
FROM sales_data_100
GROUP BY store_name, city
ORDER BY total_profit DESC
```
---

## Total Profit by Month
**ARGS:** —
```sql
SELECT STRFTIME('%Y-%m', date) AS month,
       SUM(profit) AS total_profit
FROM sales_data_100
GROUP BY month
ORDER BY month
```
---

## Average Profit Margin by Product
**ARGS:** —
```sql
SELECT product_name,
       ROUND(AVG(margin_pct), 2) AS avg_margin_pct
FROM sales_data_100
GROUP BY product_name
ORDER BY avg_margin_pct DESC
```
---

## Highest Margin Products
**ARGS:** —
```sql
SELECT product_name,
       ROUND(AVG(margin_pct), 2) AS avg_margin_pct
FROM sales_data_100
GROUP BY product_name
ORDER BY avg_margin_pct DESC
```
---

## Lowest Margin Products
**ARGS:** —
```sql
SELECT product_name,
       ROUND(AVG(margin_pct), 2) AS avg_margin_pct
FROM sales_data_100
GROUP BY product_name
ORDER BY avg_margin_pct ASC
```
---

## Top 10 Most Profitable Orders
**ARGS:** —
```sql
SELECT order_id,
       date,
       customer_name,
       product_name,
       profit
FROM sales_data_100
ORDER BY profit DESC
LIMIT 10
```
---

### 4. Customer Analysis

## Top 5 Customers by Revenue
**ARGS:** —
```sql
SELECT customer_id,
       customer_name,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY customer_id, customer_name
ORDER BY total_revenue DESC
LIMIT 5
```
---

## Top 5 Customers by Profit Generated
**ARGS:** —
```sql
SELECT customer_id,
       customer_name,
       SUM(profit) AS total_profit
FROM sales_data_100
GROUP BY customer_id, customer_name
ORDER BY total_profit DESC
LIMIT 5
```
---

## Top 5 Customers by Number of Orders
**ARGS:** —
```sql
SELECT customer_id,
       customer_name,
       COUNT(order_id) AS total_orders
FROM sales_data_100
GROUP BY customer_id, customer_name
ORDER BY total_orders DESC
LIMIT 5
```
---

## Customer Purchase Frequency
**ARGS:** —
```sql
SELECT customer_id,
       customer_name,
       COUNT(order_id) AS order_count,
       MIN(date) AS first_order_date,
       MAX(date) AS last_order_date
FROM sales_data_100
GROUP BY customer_id, customer_name
ORDER BY order_count DESC
```
---

## Customer Average Order Value
**ARGS:** —
```sql
SELECT customer_id,
       customer_name,
       ROUND(AVG(total_revenue), 2) AS avg_order_value
FROM sales_data_100
GROUP BY customer_id, customer_name
ORDER BY avg_order_value DESC
```
---

## Customers Who Bought Every Product
**ARGS:** —
```sql
SELECT customer_id,
       customer_name,
       COUNT(DISTINCT product_id) AS products_bought
FROM sales_data_100
GROUP BY customer_id, customer_name
HAVING COUNT(DISTINCT product_id) = (SELECT COUNT(DISTINCT product_id) FROM sales_data_100)
ORDER BY customer_name
```
---

### 5. Product Analysis

## Best Selling Products by Revenue
**ARGS:** —
```sql
SELECT product_name,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY product_name
ORDER BY total_revenue DESC
```
---

## Best Selling Products by Units Sold
**ARGS:** —
```sql
SELECT product_name,
       SUM(quantity) AS total_units_sold
FROM sales_data_100
GROUP BY product_name
ORDER BY total_units_sold DESC
```
---

## Least Selling Products by Units Sold
**ARGS:** —
```sql
SELECT product_name,
       SUM(quantity) AS total_units_sold
FROM sales_data_100
GROUP BY product_name
ORDER BY total_units_sold ASC
```
---

## Product Revenue Share (% of Total)
**ARGS:** —
```sql
SELECT product_name,
       SUM(total_revenue) AS product_revenue,
       ROUND(SUM(total_revenue) * 100.0 / (SELECT SUM(total_revenue) FROM sales_data_100), 2) AS revenue_share_pct
FROM sales_data_100
GROUP BY product_name
ORDER BY product_revenue DESC
```
---

## Products Sold in All Three Stores
**ARGS:** —
```sql
SELECT product_name,
       COUNT(DISTINCT store_id) AS store_count
FROM sales_data_100
GROUP BY product_name
HAVING COUNT(DISTINCT store_id) = (SELECT COUNT(DISTINCT store_id) FROM sales_data_100)
ORDER BY product_name
```
---

## Average Unit Price vs Unit Cost by Product
**ARGS:** —
```sql
SELECT product_name,
       ROUND(AVG(unit_price), 2) AS avg_unit_price,
       ROUND(AVG(unit_cost), 2) AS avg_unit_cost,
       ROUND(AVG(unit_price) - AVG(unit_cost), 2) AS avg_unit_margin
FROM sales_data_100
GROUP BY product_name
ORDER BY avg_unit_margin DESC
```
---

### 6. Store Analysis

## Revenue by Store
**ARGS:** —
```sql
SELECT store_name,
       city,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY store_name, city
ORDER BY total_revenue DESC
```
---

## Profit by Store
**ARGS:** —
```sql
SELECT store_name,
       city,
       SUM(profit) AS total_profit
FROM sales_data_100
GROUP BY store_name, city
ORDER BY total_profit DESC
```
---

## Orders per Store
**ARGS:** —
```sql
SELECT store_name,
       city,
       COUNT(order_id) AS total_orders
FROM sales_data_100
GROUP BY store_name, city
ORDER BY total_orders DESC
```
---

## Best Performing Store by Revenue
**ARGS:** —
```sql
SELECT store_name,
       city,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY store_name, city
ORDER BY total_revenue DESC
LIMIT 1
```
---

## Store with Highest Average Order Value
**ARGS:** —
```sql
SELECT store_name,
       city,
       ROUND(AVG(total_revenue), 2) AS avg_order_value
FROM sales_data_100
GROUP BY store_name, city
ORDER BY avg_order_value DESC
LIMIT 1
```
---

## Product Mix by Store
**ARGS:** —
```sql
SELECT store_name,
       product_name,
       COUNT(order_id) AS order_count,
       SUM(quantity) AS total_units,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY store_name, product_name
ORDER BY store_name, total_revenue DESC
```
---

### 7. Time-Based Analysis

## Monthly Sales Trend
**ARGS:** —
```sql
SELECT STRFTIME('%Y-%m', date) AS month,
       COUNT(order_id) AS total_orders,
       SUM(quantity) AS total_units,
       SUM(total_revenue) AS total_revenue,
       SUM(profit) AS total_profit
FROM sales_data_100
GROUP BY month
ORDER BY month
```
---

## Quarterly Revenue Summary
**ARGS:** —
```sql
SELECT STRFTIME('%Y', date) AS year,
       'Q' || CAST((CAST(STRFTIME('%m', date) AS INTEGER) - 1) / 3 + 1 AS TEXT) AS quarter,
       SUM(total_revenue) AS total_revenue,
       SUM(profit) AS total_profit,
       COUNT(order_id) AS total_orders
FROM sales_data_100
GROUP BY year, quarter
ORDER BY year, quarter
```
---

## Best Month by Revenue
**ARGS:** —
```sql
SELECT STRFTIME('%Y-%m', date) AS month,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY month
ORDER BY total_revenue DESC
LIMIT 1
```
---

## Worst Month by Revenue
**ARGS:** —
```sql
SELECT STRFTIME('%Y-%m', date) AS month,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY month
ORDER BY total_revenue ASC
LIMIT 1
```
---

## Month-over-Month Revenue Growth
**ARGS:** —
```sql
WITH monthly AS (
    SELECT STRFTIME('%Y-%m', date) AS month,
           SUM(total_revenue) AS total_revenue
    FROM sales_data_100
    GROUP BY month
),
lagged AS (
    SELECT month,
           total_revenue,
           LAG(total_revenue) OVER (ORDER BY month) AS prev_revenue
    FROM monthly
)
SELECT month,
       total_revenue,
       prev_revenue,
       ROUND((total_revenue - prev_revenue) * 100.0 / prev_revenue, 2) AS mom_growth_pct
FROM lagged
ORDER BY month
```
---

## Orders per Day of Week
**ARGS:** —
```sql
SELECT CASE CAST(STRFTIME('%w', date) AS INTEGER)
           WHEN 0 THEN 'Sunday'
           WHEN 1 THEN 'Monday'
           WHEN 2 THEN 'Tuesday'
           WHEN 3 THEN 'Wednesday'
           WHEN 4 THEN 'Thursday'
           WHEN 5 THEN 'Friday'
           WHEN 6 THEN 'Saturday'
       END AS day_of_week,
       CAST(STRFTIME('%w', date) AS INTEGER) AS day_num,
       COUNT(order_id) AS total_orders,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY day_of_week, day_num
ORDER BY day_num
```
---

### 8. Payment Method Analysis

## Revenue by Payment Method
**ARGS:** —
```sql
SELECT payment_method,
       SUM(total_revenue) AS total_revenue
FROM sales_data_100
GROUP BY payment_method
ORDER BY total_revenue DESC
```
---

## Most Used Payment Method
**ARGS:** —
```sql
SELECT payment_method,
       COUNT(order_id) AS total_orders
FROM sales_data_100
GROUP BY payment_method
ORDER BY total_orders DESC
LIMIT 1
```
---

## Average Order Value by Payment Method
**ARGS:** —
```sql
SELECT payment_method,
       ROUND(AVG(total_revenue), 2) AS avg_order_value
FROM sales_data_100
GROUP BY payment_method
ORDER BY avg_order_value DESC
```
---

## Payment Method Preference by Store
**ARGS:** —
```sql
WITH store_totals AS (
    SELECT store_name,
           COUNT(order_id) AS store_total_orders
    FROM sales_data_100
    GROUP BY store_name
)
SELECT s.store_name,
       s.payment_method,
       COUNT(s.order_id) AS total_orders,
       ROUND(COUNT(s.order_id) * 100.0 / st.store_total_orders, 2) AS pct_of_store_orders
FROM sales_data_100 s
JOIN store_totals st ON s.store_name = st.store_name
GROUP BY s.store_name, s.payment_method
ORDER BY s.store_name, total_orders DESC
```
---

### 9. Data Quality Checks

## Orders with Missing Customer Information
**ARGS:** —
```sql
SELECT order_id,
       date,
       customer_id,
       customer_name,
       product_name,
       total_revenue
FROM sales_data_100
WHERE customer_id IS NULL
   OR customer_id = ''
   OR customer_name IS NULL
   OR customer_name = ''
ORDER BY date
```
---

## Orders with Negative or Zero Quantity
**ARGS:** —
```sql
SELECT order_id,
       date,
       customer_name,
       product_name,
       quantity
FROM sales_data_100
WHERE quantity <= 0
ORDER BY quantity ASC
```
---

## Duplicate Order IDs
**ARGS:** —
```sql
SELECT order_id,
       COUNT(*) AS occurrences
FROM sales_data_100
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY occurrences DESC
```
---

## Orders with Missing Cost or Revenue Fields
**ARGS:** —
```sql
SELECT order_id,
       date,
       customer_name,
       product_name,
       unit_cost,
       total_cost,
       total_revenue,
       profit,
       margin_pct
FROM sales_data_100
WHERE unit_cost IS NULL OR unit_cost = ''
   OR total_cost IS NULL OR total_cost = ''
   OR total_revenue IS NULL OR total_revenue = ''
   OR profit IS NULL OR profit = ''
   OR margin_pct IS NULL OR margin_pct = ''
ORDER BY date
```
---

## Potential Product Name Typos
**ARGS:** —
```sql
SELECT product_name,
       COUNT(*) AS occurrences
FROM sales_data_100
GROUP BY product_name
ORDER BY occurrences ASC
```
---
