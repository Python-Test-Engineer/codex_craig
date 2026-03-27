# SQL Query Catalog
<!-- source: data/data.csv | table: data | generated: 2026-03-27 | queries: 100 -->

---

### Overview

## Total Row Count
**ARGS:** —
**Description:** Returns the total number of order line items in the dataset.
```sql
SELECT COUNT(*) AS row_count
FROM data;
```
---

## Column Sample
**ARGS:** —
**Description:** Returns the first 10 rows to preview the full dataset structure.
```sql
SELECT *
FROM data
LIMIT 10;
```
---

## Distinct Value Count per Categorical Column
**ARGS:** —
**Description:** Shows cardinality for PRODUCTLINE, STATUS, TERRITORY, DEALSIZE, COUNTRY, and CITY.
```sql
SELECT
    COUNT(DISTINCT PRODUCTLINE) AS distinct_PRODUCTLINE,
    COUNT(DISTINCT STATUS) AS distinct_STATUS,
    COUNT(DISTINCT TERRITORY) AS distinct_TERRITORY,
    COUNT(DISTINCT DEALSIZE) AS distinct_DEALSIZE,
    COUNT(DISTINCT COUNTRY) AS distinct_COUNTRY,
    COUNT(DISTINCT CITY) AS distinct_CITY
FROM data;
```
---

## Date Range of Orders
**ARGS:** —
**Description:** Returns the earliest and latest ORDERDATE in the dataset.
```sql
SELECT
    MIN(ORDERDATE) AS earliest_order,
    MAX(ORDERDATE) AS latest_order
FROM data;
```
---

## Summary Statistics for Key Measures
**ARGS:** —
**Description:** Returns min, max, avg, and total for SALES, QUANTITYORDERED, and PRICEEACH.
```sql
SELECT
    MIN(SALES) AS min_SALES,
    MAX(SALES) AS max_SALES,
    ROUND(AVG(SALES), 2) AS avg_SALES,
    ROUND(SUM(SALES), 2) AS total_SALES,
    MIN(QUANTITYORDERED) AS min_QUANTITYORDERED,
    MAX(QUANTITYORDERED) AS max_QUANTITYORDERED,
    ROUND(AVG(QUANTITYORDERED), 2) AS avg_QUANTITYORDERED,
    MIN(PRICEEACH) AS min_PRICEEACH,
    MAX(PRICEEACH) AS max_PRICEEACH,
    ROUND(AVG(PRICEEACH), 2) AS avg_PRICEEACH
FROM data;
```
---

### Revenue & Sales

## Total Sales Revenue
**ARGS:** —
**Description:** Shows the combined sum of all SALES across the entire dataset.
```sql
SELECT ROUND(SUM(SALES), 2) AS total_revenue
FROM data;
```
---

## Total Revenue by PRODUCTLINE
**ARGS:** —
**Description:** Ranks each product line by total SALES generated, highest first.
```sql
SELECT
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(*) AS order_lines,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY PRODUCTLINE
ORDER BY total_revenue DESC;
```
---

## Total Revenue by CUSTOMERNAME
**ARGS:** —
**Description:** Ranks each customer by total SALES generated, highest first.
```sql
SELECT
    CUSTOMERNAME,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY CUSTOMERNAME
ORDER BY total_revenue DESC;
```
---

## Total Revenue by COUNTRY
**ARGS:** —
**Description:** Ranks each country by total SALES generated, highest first.
```sql
SELECT
    COUNTRY,
    TERRITORY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY COUNTRY, TERRITORY
ORDER BY total_revenue DESC;
```
---

## Total Revenue by TERRITORY
**ARGS:** —
**Description:** Ranks each sales territory (NA, EMEA, APAC, Japan) by total SALES.
```sql
SELECT
    TERRITORY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY TERRITORY
ORDER BY total_revenue DESC;
```
---

## Total Revenue by CITY
**ARGS:** —
**Description:** Ranks each city by total SALES, highest first.
```sql
SELECT
    CITY,
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count
FROM data
GROUP BY CITY, COUNTRY
ORDER BY total_revenue DESC;
```
---

## Total Revenue by DEALSIZE
**ARGS:** —
**Description:** Compares total SALES across Small, Medium, and Large deal sizes.
```sql
SELECT
    DEALSIZE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(*) AS order_lines,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    ROUND(AVG(SALES), 2) AS avg_sale
FROM data
GROUP BY DEALSIZE
ORDER BY total_revenue DESC;
```
---

## Total Revenue by PRODUCTCODE
**ARGS:** —
**Description:** Ranks each product code by total SALES, highest first.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_revenue DESC;
```
---

## Average Revenue per Order Line
**ARGS:** —
**Description:** Shows the mean SALES value per individual order line.
```sql
SELECT ROUND(AVG(SALES), 2) AS avg_revenue_per_line
FROM data;
```
---

## Average PRICEEACH by PRODUCTLINE
**ARGS:** —
**Description:** Compares average unit selling price across product lines.
```sql
SELECT
    PRODUCTLINE,
    ROUND(AVG(PRICEEACH), 2) AS avg_price,
    ROUND(MIN(PRICEEACH), 2) AS min_price,
    ROUND(MAX(PRICEEACH), 2) AS max_price
FROM data
GROUP BY PRODUCTLINE
ORDER BY avg_price DESC;
```
---

## Revenue by Year
**ARGS:** —
**Description:** Shows total SALES grouped by YEAR_ID to compare annual performance.
```sql
SELECT
    YEAR_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY YEAR_ID
ORDER BY YEAR_ID;
```
---

## Revenue by Quarter
**ARGS:** —
**Description:** Shows total SALES grouped by QTR_ID to reveal quarterly patterns.
```sql
SELECT
    QTR_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY QTR_ID
ORDER BY QTR_ID;
```
---

### Volume & Orders

## Total Units Ordered
**ARGS:** —
**Description:** Shows the sum of QUANTITYORDERED across all order lines.
```sql
SELECT SUM(QUANTITYORDERED) AS total_units_ordered
FROM data;
```
---

## Total Units by PRODUCTLINE
**ARGS:** —
**Description:** Ranks each product line by total QUANTITYORDERED, highest first.
```sql
SELECT
    PRODUCTLINE,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(*) AS order_lines,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY PRODUCTLINE
ORDER BY total_units DESC;
```
---

## Total Units by CUSTOMERNAME
**ARGS:** —
**Description:** Ranks each customer by total QUANTITYORDERED, highest first.
```sql
SELECT
    CUSTOMERNAME,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY CUSTOMERNAME
ORDER BY total_units DESC;
```
---

## Total Units by PRODUCTCODE
**ARGS:** —
**Description:** Ranks each product code by total QUANTITYORDERED, highest first.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(*) AS order_lines
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_units DESC;
```
---

## Total Distinct Order Count
**ARGS:** —
**Description:** Returns the number of unique ORDERNUMBER values in the dataset.
```sql
SELECT COUNT(DISTINCT ORDERNUMBER) AS distinct_orders
FROM data;
```
---

## Order Line Count by STATUS
**ARGS:** —
**Description:** Shows how many order lines fall under each STATUS value.
```sql
SELECT
    STATUS,
    COUNT(*) AS order_lines,
    COUNT(DISTINCT ORDERNUMBER) AS distinct_orders,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY STATUS
ORDER BY order_lines DESC;
```
---

## Average Quantity per Order Line
**ARGS:** —
**Description:** Returns the mean QUANTITYORDERED per line item.
```sql
SELECT ROUND(AVG(QUANTITYORDERED), 2) AS avg_quantity_per_line
FROM data;
```
---

## Orders with Most Line Items
**ARGS:** —
**Description:** Ranks orders by number of line items, identifying large complex orders.
```sql
SELECT
    ORDERNUMBER,
    COUNT(*) AS line_item_count,
    ROUND(SUM(SALES), 2) AS total_order_revenue,
    MAX(CUSTOMERNAME) AS customer
FROM data
GROUP BY ORDERNUMBER
ORDER BY line_item_count DESC
LIMIT 20;
```
---

### Customer Analysis

## Customers Ranked by Total Revenue
**ARGS:** —
**Description:** Ranks all customers by lifetime SALES, highest first, with order count.
```sql
SELECT
    CUSTOMERNAME,
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY CUSTOMERNAME, COUNTRY
ORDER BY total_revenue DESC;
```
---

## Customers Ranked by Total Units Ordered
**ARGS:** —
**Description:** Ranks customers by total QUANTITYORDERED, highest first.
```sql
SELECT
    CUSTOMERNAME,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY CUSTOMERNAME
ORDER BY total_units DESC;
```
---

## Customers Ranked by Order Count
**ARGS:** —
**Description:** Ranks customers by number of distinct orders placed, highest first.
```sql
SELECT
    CUSTOMERNAME,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY CUSTOMERNAME
ORDER BY order_count DESC;
```
---

## Top 5 Customers by Revenue
**ARGS:** —
**Description:** Lists the 5 highest-revenue customers with total SALES and order count.
```sql
SELECT
    CUSTOMERNAME,
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY CUSTOMERNAME, COUNTRY
ORDER BY total_revenue DESC
LIMIT 5;
```
---

## Bottom 5 Customers by Revenue
**ARGS:** —
**Description:** Lists the 5 lowest-revenue customers to identify underperformers.
```sql
SELECT
    CUSTOMERNAME,
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY CUSTOMERNAME, COUNTRY
ORDER BY total_revenue ASC
LIMIT 5;
```
---

## Customer Count by COUNTRY
**ARGS:** —
**Description:** Counts distinct customers per country, ordered by count descending.
```sql
SELECT
    COUNTRY,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count
FROM data
GROUP BY COUNTRY
ORDER BY customer_count DESC;
```
---

## Customer Count by TERRITORY
**ARGS:** —
**Description:** Counts distinct customers per territory.
```sql
SELECT
    TERRITORY,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count
FROM data
GROUP BY TERRITORY
ORDER BY customer_count DESC;
```
---

## Average Revenue per Customer
**ARGS:** —
**Description:** Returns mean total lifetime SALES across all customers.
```sql
SELECT ROUND(AVG(customer_total), 2) AS avg_revenue_per_customer
FROM (
    SELECT CUSTOMERNAME, SUM(SALES) AS customer_total
    FROM data
    GROUP BY CUSTOMERNAME
);
```
---

## Repeat vs One-Time Customers
**ARGS:** —
**Description:** Counts customers with more than one order versus exactly one order.
```sql
SELECT
    CASE WHEN order_count > 1 THEN 'Repeat' ELSE 'One-Time' END AS customer_type,
    COUNT(*) AS customer_count
FROM (
    SELECT CUSTOMERNAME, COUNT(DISTINCT ORDERNUMBER) AS order_count
    FROM data
    GROUP BY CUSTOMERNAME
)
GROUP BY customer_type;
```
---

## Customers with Total Revenue Above :threshold
**ARGS:** threshold
**Description:** Lists customers whose lifetime SALES exceed a given value.
```sql
SELECT
    CUSTOMERNAME,
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY CUSTOMERNAME, COUNTRY
HAVING SUM(SALES) > :threshold
ORDER BY total_revenue DESC;
```
---

### Product Analysis

## Products Ranked by Total Revenue
**ARGS:** —
**Description:** Ranks each PRODUCTCODE by total SALES, highest first.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_revenue DESC;
```
---

## Products Ranked by Total Units Sold
**ARGS:** —
**Description:** Ranks each PRODUCTCODE by total QUANTITYORDERED, highest first.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    SUM(QUANTITYORDERED) AS total_units,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_units DESC;
```
---

## Top 5 Products by Revenue
**ARGS:** —
**Description:** Lists the 5 highest-revenue products with total sales and units.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_revenue DESC
LIMIT 5;
```
---

## Bottom 5 Products by Revenue
**ARGS:** —
**Description:** Lists the 5 lowest-revenue products to identify slow sellers.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_revenue ASC
LIMIT 5;
```
---

## Top 3 Products by Revenue
**ARGS:** —
**Description:** Lists the 3 highest-revenue products for quick-reference ranking.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_revenue DESC
LIMIT 3;
```
---

## Top 10 Products by Revenue
**ARGS:** —
**Description:** Lists the 10 highest-revenue products for broader analysis.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_revenue DESC
LIMIT 10;
```
---

## Product Lines Ranked by Total Revenue
**ARGS:** —
**Description:** Ranks product lines by total SALES with units and order count.
```sql
SELECT
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    COUNT(DISTINCT PRODUCTCODE) AS product_count
FROM data
GROUP BY PRODUCTLINE
ORDER BY total_revenue DESC;
```
---

## Product Lines Ranked by Total Units Sold
**ARGS:** —
**Description:** Ranks product lines by total QUANTITYORDERED, highest first.
```sql
SELECT
    PRODUCTLINE,
    SUM(QUANTITYORDERED) AS total_units,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY PRODUCTLINE
ORDER BY total_units DESC;
```
---

## Average PRICEEACH vs MSRP by PRODUCTCODE
**ARGS:** —
**Description:** Compares average actual selling price against MSRP to reveal discount per product.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(AVG(PRICEEACH), 2) AS avg_price,
    MAX(MSRP) AS msrp,
    ROUND(MAX(MSRP) - AVG(PRICEEACH), 2) AS avg_discount,
    ROUND((MAX(MSRP) - AVG(PRICEEACH)) / MAX(MSRP) * 100, 1) AS discount_pct
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY discount_pct DESC;
```
---

## Products Selling Below MSRP on Average
**ARGS:** —
**Description:** Flags products where average PRICEEACH is less than MSRP.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(AVG(PRICEEACH), 2) AS avg_price,
    MAX(MSRP) AS msrp,
    ROUND(MAX(MSRP) - AVG(PRICEEACH), 2) AS avg_discount
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
HAVING AVG(PRICEEACH) < MAX(MSRP)
ORDER BY avg_discount DESC;
```
---

### Territory & Country Analysis

## Countries Ranked by Total Revenue
**ARGS:** —
**Description:** Ranks each country by total SALES, highest first.
```sql
SELECT
    COUNTRY,
    TERRITORY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY COUNTRY, TERRITORY
ORDER BY total_revenue DESC;
```
---

## Countries Ranked by Total Units Ordered
**ARGS:** —
**Description:** Ranks each country by total QUANTITYORDERED, highest first.
```sql
SELECT
    COUNTRY,
    SUM(QUANTITYORDERED) AS total_units,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY COUNTRY
ORDER BY total_units DESC;
```
---

## Territories Ranked by Total Revenue
**ARGS:** —
**Description:** Ranks NA, EMEA, APAC, Japan by total SALES.
```sql
SELECT
    TERRITORY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY TERRITORY
ORDER BY total_revenue DESC;
```
---

## Revenue by Territory and Country
**ARGS:** —
**Description:** Shows total SALES for each country grouped within its territory.
```sql
SELECT
    TERRITORY,
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count
FROM data
GROUP BY TERRITORY, COUNTRY
ORDER BY TERRITORY, total_revenue DESC;
```
---

## Cities Ranked by Total Revenue
**ARGS:** —
**Description:** Ranks cities by total SALES, highest first.
```sql
SELECT
    CITY,
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count
FROM data
GROUP BY CITY, COUNTRY
ORDER BY total_revenue DESC;
```
---

## Top 5 Countries by Revenue
**ARGS:** —
**Description:** Lists the 5 highest-revenue countries with total SALES.
```sql
SELECT
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count
FROM data
GROUP BY COUNTRY
ORDER BY total_revenue DESC
LIMIT 5;
```
---

## Bottom 5 Countries by Revenue
**ARGS:** —
**Description:** Lists the 5 lowest-revenue countries to identify weak markets.
```sql
SELECT
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count
FROM data
GROUP BY COUNTRY
ORDER BY total_revenue ASC
LIMIT 5;
```
---

## Customer Count and Revenue by Territory
**ARGS:** —
**Description:** Shows distinct customer count and total SALES per territory.
```sql
SELECT
    TERRITORY,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY TERRITORY
ORDER BY total_revenue DESC;
```
---

### Time-Based Analysis

## Monthly Revenue Trend
**ARGS:** —
**Description:** Returns total SALES grouped by year-month, ordered chronologically.
```sql
SELECT
    YEAR_ID,
    MONTH_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY YEAR_ID, MONTH_ID
ORDER BY YEAR_ID, MONTH_ID;
```
---

## Yearly Revenue Total
**ARGS:** —
**Description:** Shows total SALES per YEAR_ID to compare 2003, 2004, and 2005.
```sql
SELECT
    YEAR_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units
FROM data
GROUP BY YEAR_ID
ORDER BY YEAR_ID;
```
---

## Quarterly Revenue by Year
**ARGS:** —
**Description:** Shows SALES per quarter per year to reveal seasonal patterns.
```sql
SELECT
    YEAR_ID,
    QTR_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY YEAR_ID, QTR_ID
ORDER BY YEAR_ID, QTR_ID;
```
---

## Monthly Revenue by PRODUCTLINE
**ARGS:** —
**Description:** Shows monthly SALES trend broken down by product line.
```sql
SELECT
    YEAR_ID,
    MONTH_ID,
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY YEAR_ID, MONTH_ID, PRODUCTLINE
ORDER BY YEAR_ID, MONTH_ID, total_revenue DESC;
```
---

## Best Month by Revenue
**ARGS:** —
**Description:** Identifies the single year-month with the highest total SALES.
```sql
SELECT
    YEAR_ID,
    MONTH_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY YEAR_ID, MONTH_ID
ORDER BY total_revenue DESC
LIMIT 1;
```
---

## Revenue Between :start_date and :end_date
**ARGS:** start_date, end_date
**Description:** Returns total SALES within an arbitrary date range.
```sql
SELECT
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units
FROM data
WHERE ORDERDATE >= :start_date AND ORDERDATE <= :end_date;
```
---

## Transactions Between :start_date and :end_date
**ARGS:** start_date, end_date
**Description:** Returns all order lines within a specified date range.
```sql
SELECT *
FROM data
WHERE ORDERDATE >= :start_date AND ORDERDATE <= :end_date
ORDER BY ORDERDATE;
```
---

## Revenue for :year
**ARGS:** year
**Description:** Returns total SALES for a specific four-digit year.
```sql
SELECT
    YEAR_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units
FROM data
WHERE YEAR_ID = :year
GROUP BY YEAR_ID;
```
---

## Revenue for :year_month
**ARGS:** year_id, month_id
**Description:** Returns total SALES for a specific year and month combination.
```sql
SELECT
    YEAR_ID,
    MONTH_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
WHERE YEAR_ID = :year_id AND MONTH_ID = :month_id
GROUP BY YEAR_ID, MONTH_ID;
```
---

## Month-over-Month Revenue Change
**ARGS:** —
**Description:** Compares each month's total SALES against the prior month using self-join.
```sql
SELECT
    t1.YEAR_ID,
    t1.MONTH_ID,
    ROUND(t1.monthly_revenue, 2) AS revenue,
    ROUND(t2.monthly_revenue, 2) AS prior_month_revenue,
    ROUND((t1.monthly_revenue - t2.monthly_revenue) / t2.monthly_revenue * 100, 1) AS pct_change
FROM (
    SELECT YEAR_ID, MONTH_ID, SUM(SALES) AS monthly_revenue
    FROM data
    GROUP BY YEAR_ID, MONTH_ID
) t1
LEFT JOIN (
    SELECT YEAR_ID, MONTH_ID, SUM(SALES) AS monthly_revenue
    FROM data
    GROUP BY YEAR_ID, MONTH_ID
) t2
ON (t1.YEAR_ID = t2.YEAR_ID AND t1.MONTH_ID = t2.MONTH_ID + 1)
OR (t1.YEAR_ID = t2.YEAR_ID + 1 AND t1.MONTH_ID = 1 AND t2.MONTH_ID = 12)
ORDER BY t1.YEAR_ID, t1.MONTH_ID;
```
---

### Status & Deal Size Analysis

## Revenue by STATUS
**ARGS:** —
**Description:** Shows total SALES grouped by order STATUS (Shipped, Disputed, Cancelled, etc.).
```sql
SELECT
    STATUS,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(*) AS order_lines,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
GROUP BY STATUS
ORDER BY total_revenue DESC;
```
---

## Order Count by STATUS
**ARGS:** —
**Description:** Counts order lines per STATUS to show order pipeline distribution.
```sql
SELECT
    STATUS,
    COUNT(*) AS order_lines,
    COUNT(DISTINCT ORDERNUMBER) AS distinct_orders
FROM data
GROUP BY STATUS
ORDER BY order_lines DESC;
```
---

## Disputed Orders by CUSTOMERNAME
**ARGS:** —
**Description:** Lists customers with Disputed status orders and their total disputed SALES.
```sql
SELECT
    CUSTOMERNAME,
    COUNT(DISTINCT ORDERNUMBER) AS disputed_orders,
    ROUND(SUM(SALES), 2) AS total_disputed_revenue
FROM data
WHERE STATUS = 'Disputed'
GROUP BY CUSTOMERNAME
ORDER BY total_disputed_revenue DESC;
```
---

## Revenue by DEALSIZE
**ARGS:** —
**Description:** Shows total SALES, order count, and avg SALES per deal size category.
```sql
SELECT
    DEALSIZE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    ROUND(AVG(SALES), 2) AS avg_sale_per_line
FROM data
GROUP BY DEALSIZE
ORDER BY total_revenue DESC;
```
---

## DEALSIZE Distribution by PRODUCTLINE
**ARGS:** —
**Description:** Shows count of Small, Medium, Large deals for each product line.
```sql
SELECT
    PRODUCTLINE,
    DEALSIZE,
    COUNT(*) AS order_lines,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY PRODUCTLINE, DEALSIZE
ORDER BY PRODUCTLINE, DEALSIZE;
```
---

## Cancelled or On Hold Orders
**ARGS:** —
**Description:** Returns all order lines with STATUS = Cancelled or On Hold.
```sql
SELECT
    ORDERNUMBER,
    CUSTOMERNAME,
    PRODUCTCODE,
    SALES,
    QUANTITYORDERED,
    ORDERDATE,
    STATUS
FROM data
WHERE STATUS IN ('Cancelled', 'On Hold')
ORDER BY ORDERNUMBER;
```
---

### Parametric Lookups

## All Transactions for CUSTOMERNAME = :customer_name
**ARGS:** customer_name
**Description:** Returns all order lines for a specific customer ordered by date.
```sql
SELECT *
FROM data
WHERE CUSTOMERNAME = :customer_name
ORDER BY ORDERDATE;
```
---

## Revenue Summary for CUSTOMERNAME = :customer_name
**ARGS:** customer_name
**Description:** Returns total SALES, orders, and units for one specific customer.
```sql
SELECT
    CUSTOMERNAME,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units,
    ROUND(AVG(SALES), 2) AS avg_sale_per_line
FROM data
WHERE CUSTOMERNAME = :customer_name
GROUP BY CUSTOMERNAME;
```
---

## Full Performance for CUSTOMERNAME = :customer_name
**ARGS:** customer_name
**Description:** Shows SALES, units, avg price, and order count for one customer.
```sql
SELECT
    CUSTOMERNAME,
    COUNTRY,
    TERRITORY,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    COUNT(*) AS order_lines,
    SUM(QUANTITYORDERED) AS total_units,
    ROUND(SUM(SALES), 2) AS total_revenue,
    ROUND(AVG(SALES), 2) AS avg_line_revenue,
    ROUND(AVG(PRICEEACH), 2) AS avg_price
FROM data
WHERE CUSTOMERNAME = :customer_name
GROUP BY CUSTOMERNAME, COUNTRY, TERRITORY;
```
---

## Top Products for CUSTOMERNAME = :customer_name
**ARGS:** customer_name
**Description:** Ranks products by SALES for one specific customer.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    SUM(QUANTITYORDERED) AS total_units,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
WHERE CUSTOMERNAME = :customer_name
GROUP BY PRODUCTCODE, PRODUCTLINE
ORDER BY total_revenue DESC;
```
---

## Monthly Revenue Trend for CUSTOMERNAME = :customer_name
**ARGS:** customer_name
**Description:** Shows monthly SALES trend for one customer.
```sql
SELECT
    YEAR_ID,
    MONTH_ID,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units
FROM data
WHERE CUSTOMERNAME = :customer_name
GROUP BY YEAR_ID, MONTH_ID
ORDER BY YEAR_ID, MONTH_ID;
```
---

## All Transactions for PRODUCTCODE = :product_code
**ARGS:** product_code
**Description:** Returns all order lines for a specific product code.
```sql
SELECT *
FROM data
WHERE PRODUCTCODE = :product_code
ORDER BY ORDERDATE;
```
---

## Revenue Summary for PRODUCTCODE = :product_code
**ARGS:** product_code
**Description:** Returns total SALES, units, and avg price for one product.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units,
    ROUND(AVG(PRICEEACH), 2) AS avg_price,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
WHERE PRODUCTCODE = :product_code
GROUP BY PRODUCTCODE, PRODUCTLINE;
```
---

## Top Customers for PRODUCTCODE = :product_code
**ARGS:** product_code
**Description:** Ranks customers by SALES for a specific product code.
```sql
SELECT
    CUSTOMERNAME,
    COUNTRY,
    SUM(QUANTITYORDERED) AS total_units,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
WHERE PRODUCTCODE = :product_code
GROUP BY CUSTOMERNAME, COUNTRY
ORDER BY total_revenue DESC;
```
---

## All Transactions for COUNTRY = :country
**ARGS:** country
**Description:** Returns all order lines for a specific country ordered by date.
```sql
SELECT *
FROM data
WHERE COUNTRY = :country
ORDER BY ORDERDATE;
```
---

## Revenue Summary for COUNTRY = :country
**ARGS:** country
**Description:** Returns total SALES, order count, and units for one country.
```sql
SELECT
    COUNTRY,
    TERRITORY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count
FROM data
WHERE COUNTRY = :country
GROUP BY COUNTRY, TERRITORY;
```
---

## Revenue and Orders for PRODUCTLINE = :product_line
**ARGS:** product_line
**Description:** Returns total SALES, units, and order count for one product line.
```sql
SELECT
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    COUNT(DISTINCT PRODUCTCODE) AS product_count
FROM data
WHERE PRODUCTLINE = :product_line
GROUP BY PRODUCTLINE;
```
---

## Revenue Summary for TERRITORY = :territory
**ARGS:** territory
**Description:** Returns total SALES, customer count, and units for one territory.
```sql
SELECT
    TERRITORY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT CUSTOMERNAME) AS customer_count,
    SUM(QUANTITYORDERED) AS total_units,
    COUNT(DISTINCT ORDERNUMBER) AS order_count
FROM data
WHERE TERRITORY = :territory
GROUP BY TERRITORY;
```
---

## Revenue and Orders for DEALSIZE = :deal_size
**ARGS:** deal_size
**Description:** Returns total SALES and order count for a specific deal size.
```sql
SELECT
    DEALSIZE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    COUNT(*) AS order_lines,
    ROUND(AVG(SALES), 2) AS avg_sale
FROM data
WHERE DEALSIZE = :deal_size
GROUP BY DEALSIZE;
```
---

## Orders Above :min_revenue
**ARGS:** min_revenue
**Description:** Returns all order lines where SALES exceed a given minimum threshold.
```sql
SELECT
    ORDERNUMBER,
    CUSTOMERNAME,
    PRODUCTCODE,
    SALES,
    ORDERDATE,
    STATUS
FROM data
WHERE SALES > :min_revenue
ORDER BY SALES DESC;
```
---

## Revenue for CUSTOMERNAME = :customer_name in COUNTRY = :country
**ARGS:** customer_name, country
**Description:** Returns SALES filtered to a specific customer-country combination.
```sql
SELECT
    CUSTOMERNAME,
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    SUM(QUANTITYORDERED) AS total_units
FROM data
WHERE CUSTOMERNAME = :customer_name AND COUNTRY = :country
GROUP BY CUSTOMERNAME, COUNTRY;
```
---

### Advanced Analytics

## Revenue Share % by PRODUCTLINE
**ARGS:** —
**Description:** Shows each product line's SALES as a percentage of the grand total.
```sql
SELECT
    PRODUCTLINE,
    ROUND(SUM(SALES), 2) AS total_revenue,
    ROUND(SUM(SALES) * 100.0 / (SELECT SUM(SALES) FROM data), 2) AS revenue_share_pct
FROM data
GROUP BY PRODUCTLINE
ORDER BY revenue_share_pct DESC;
```
---

## Revenue Share % by CUSTOMERNAME
**ARGS:** —
**Description:** Shows each customer's SALES contribution as a percentage of total revenue.
```sql
SELECT
    CUSTOMERNAME,
    ROUND(SUM(SALES), 2) AS total_revenue,
    ROUND(SUM(SALES) * 100.0 / (SELECT SUM(SALES) FROM data), 2) AS revenue_share_pct
FROM data
GROUP BY CUSTOMERNAME
ORDER BY revenue_share_pct DESC;
```
---

## Revenue Share % by COUNTRY
**ARGS:** —
**Description:** Shows each country's SALES as a percentage of the grand total.
```sql
SELECT
    COUNTRY,
    ROUND(SUM(SALES), 2) AS total_revenue,
    ROUND(SUM(SALES) * 100.0 / (SELECT SUM(SALES) FROM data), 2) AS revenue_share_pct
FROM data
GROUP BY COUNTRY
ORDER BY revenue_share_pct DESC;
```
---

## Cumulative Revenue Over Time
**ARGS:** —
**Description:** Shows running total of SALES ordered chronologically using self-join.
```sql
SELECT
    t1.YEAR_ID,
    t1.MONTH_ID,
    ROUND(t1.monthly_revenue, 2) AS monthly_revenue,
    ROUND(SUM(t2.monthly_revenue), 2) AS cumulative_revenue
FROM (
    SELECT YEAR_ID, MONTH_ID, SUM(SALES) AS monthly_revenue
    FROM data
    GROUP BY YEAR_ID, MONTH_ID
) t1
JOIN (
    SELECT YEAR_ID, MONTH_ID, SUM(SALES) AS monthly_revenue
    FROM data
    GROUP BY YEAR_ID, MONTH_ID
) t2
ON (t2.YEAR_ID < t1.YEAR_ID)
OR (t2.YEAR_ID = t1.YEAR_ID AND t2.MONTH_ID <= t1.MONTH_ID)
GROUP BY t1.YEAR_ID, t1.MONTH_ID, t1.monthly_revenue
ORDER BY t1.YEAR_ID, t1.MONTH_ID;
```
---

## Customer Revenue vs Dataset Average
**ARGS:** —
**Description:** Compares each customer's total SALES against the overall dataset average.
```sql
SELECT
    CUSTOMERNAME,
    ROUND(SUM(SALES), 2) AS customer_revenue,
    ROUND((SELECT AVG(s) FROM (SELECT SUM(SALES) AS s FROM data GROUP BY CUSTOMERNAME)), 2) AS dataset_avg,
    ROUND(SUM(SALES) - (SELECT AVG(s) FROM (SELECT SUM(SALES) AS s FROM data GROUP BY CUSTOMERNAME)), 2) AS diff_from_avg
FROM data
GROUP BY CUSTOMERNAME
ORDER BY customer_revenue DESC;
```
---

## Product Revenue as % of PRODUCTLINE Total
**ARGS:** —
**Description:** Shows each product's SALES share within its own product line.
```sql
SELECT
    p.PRODUCTCODE,
    p.PRODUCTLINE,
    ROUND(p.product_revenue, 2) AS product_revenue,
    ROUND(p.product_revenue * 100.0 / pl.line_total, 2) AS pct_of_productline
FROM (
    SELECT PRODUCTCODE, PRODUCTLINE, SUM(SALES) AS product_revenue
    FROM data
    GROUP BY PRODUCTCODE, PRODUCTLINE
) p
JOIN (
    SELECT PRODUCTLINE, SUM(SALES) AS line_total
    FROM data
    GROUP BY PRODUCTLINE
) pl ON p.PRODUCTLINE = pl.PRODUCTLINE
ORDER BY p.PRODUCTLINE, pct_of_productline DESC;
```
---

## Average Order Value by CUSTOMERNAME
**ARGS:** —
**Description:** Shows average SALES per distinct order for each customer.
```sql
SELECT
    CUSTOMERNAME,
    COUNT(DISTINCT ORDERNUMBER) AS order_count,
    ROUND(SUM(SALES) / COUNT(DISTINCT ORDERNUMBER), 2) AS avg_order_value,
    ROUND(SUM(SALES), 2) AS total_revenue
FROM data
GROUP BY CUSTOMERNAME
ORDER BY avg_order_value DESC;
```
---

## Pareto: Customers Generating Top 80% of Revenue
**ARGS:** —
**Description:** Identifies the high-value customer segment using CTE and running sum.
```sql
WITH customer_revenue AS (
    SELECT
        CUSTOMERNAME,
        SUM(SALES) AS total_revenue
    FROM data
    GROUP BY CUSTOMERNAME
    ORDER BY total_revenue DESC
),
running_total AS (
    SELECT
        CUSTOMERNAME,
        total_revenue,
        SUM(total_revenue) OVER (ORDER BY total_revenue DESC) AS cumulative_revenue,
        SUM(total_revenue) OVER () AS grand_total
    FROM customer_revenue
)
SELECT
    CUSTOMERNAME,
    ROUND(total_revenue, 2) AS total_revenue,
    ROUND(cumulative_revenue, 2) AS cumulative_revenue,
    ROUND(cumulative_revenue * 100.0 / grand_total, 1) AS cumulative_pct
FROM running_total
WHERE cumulative_revenue - total_revenue < grand_total * 0.8
ORDER BY total_revenue DESC;
```
---

### Data Quality Checks

## NULL Count per Column
**ARGS:** —
**Description:** Counts NULL values in each column, ordered by count descending.
```sql
SELECT
    SUM(CASE WHEN ORDERNUMBER IS NULL THEN 1 ELSE 0 END) AS null_ORDERNUMBER,
    SUM(CASE WHEN QUANTITYORDERED IS NULL THEN 1 ELSE 0 END) AS null_QUANTITYORDERED,
    SUM(CASE WHEN PRICEEACH IS NULL THEN 1 ELSE 0 END) AS null_PRICEEACH,
    SUM(CASE WHEN SALES IS NULL THEN 1 ELSE 0 END) AS null_SALES,
    SUM(CASE WHEN ORDERDATE IS NULL THEN 1 ELSE 0 END) AS null_ORDERDATE,
    SUM(CASE WHEN STATUS IS NULL THEN 1 ELSE 0 END) AS null_STATUS,
    SUM(CASE WHEN PRODUCTLINE IS NULL THEN 1 ELSE 0 END) AS null_PRODUCTLINE,
    SUM(CASE WHEN PRODUCTCODE IS NULL THEN 1 ELSE 0 END) AS null_PRODUCTCODE,
    SUM(CASE WHEN CUSTOMERNAME IS NULL THEN 1 ELSE 0 END) AS null_CUSTOMERNAME,
    SUM(CASE WHEN COUNTRY IS NULL THEN 1 ELSE 0 END) AS null_COUNTRY,
    SUM(CASE WHEN TERRITORY IS NULL THEN 1 ELSE 0 END) AS null_TERRITORY,
    SUM(CASE WHEN DEALSIZE IS NULL THEN 1 ELSE 0 END) AS null_DEALSIZE,
    SUM(CASE WHEN ADDRESSLINE2 IS NULL THEN 1 ELSE 0 END) AS null_ADDRESSLINE2,
    SUM(CASE WHEN STATE IS NULL THEN 1 ELSE 0 END) AS null_STATE
FROM data;
```
---

## Duplicate ORDERNUMBER + ORDERLINENUMBER Combinations
**ARGS:** —
**Description:** Flags any order line combinations that appear more than once.
```sql
SELECT
    ORDERNUMBER,
    ORDERLINENUMBER,
    COUNT(*) AS occurrences
FROM data
GROUP BY ORDERNUMBER, ORDERLINENUMBER
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;
```
---

## Negative SALES Values
**ARGS:** —
**Description:** Flags rows where SALES is negative, indicating potential data entry errors.
```sql
SELECT
    ORDERNUMBER,
    ORDERLINENUMBER,
    CUSTOMERNAME,
    PRODUCTCODE,
    SALES,
    ORDERDATE
FROM data
WHERE SALES < 0
ORDER BY SALES;
```
---

## Negative QUANTITYORDERED Values
**ARGS:** —
**Description:** Flags rows where QUANTITYORDERED is less than zero.
```sql
SELECT
    ORDERNUMBER,
    ORDERLINENUMBER,
    CUSTOMERNAME,
    PRODUCTCODE,
    QUANTITYORDERED,
    ORDERDATE
FROM data
WHERE QUANTITYORDERED < 0
ORDER BY QUANTITYORDERED;
```
---

## SALES Calculation Validation
**ARGS:** —
**Description:** Flags rows where SALES differs from QUANTITYORDERED × PRICEEACH by more than 1.
```sql
SELECT
    ORDERNUMBER,
    ORDERLINENUMBER,
    CUSTOMERNAME,
    PRODUCTCODE,
    QUANTITYORDERED,
    PRICEEACH,
    SALES,
    ROUND(QUANTITYORDERED * PRICEEACH, 2) AS calculated_sales,
    ROUND(SALES - QUANTITYORDERED * PRICEEACH, 2) AS discrepancy
FROM data
WHERE ABS(SALES - QUANTITYORDERED * PRICEEACH) > 1
ORDER BY ABS(SALES - QUANTITYORDERED * PRICEEACH) DESC;
```
---

## Price Below MSRP Check
**ARGS:** —
**Description:** Lists products where average PRICEEACH is less than MSRP, showing discount magnitude.
```sql
SELECT
    PRODUCTCODE,
    PRODUCTLINE,
    ROUND(AVG(PRICEEACH), 2) AS avg_price,
    MAX(MSRP) AS msrp,
    ROUND(MAX(MSRP) - AVG(PRICEEACH), 2) AS discount_amount,
    ROUND((MAX(MSRP) - AVG(PRICEEACH)) / MAX(MSRP) * 100, 1) AS discount_pct
FROM data
GROUP BY PRODUCTCODE, PRODUCTLINE
HAVING AVG(PRICEEACH) < MAX(MSRP)
ORDER BY discount_pct DESC;
```
---

## Outlier SALES Rows
**ARGS:** —
**Description:** Returns rows where SALES is more than 3 times the dataset average.
```sql
SELECT
    ORDERNUMBER,
    ORDERLINENUMBER,
    CUSTOMERNAME,
    PRODUCTCODE,
    SALES,
    ROUND((SELECT AVG(SALES) FROM data), 2) AS dataset_avg,
    ROUND(SALES / (SELECT AVG(SALES) FROM data), 1) AS times_avg
FROM data
WHERE SALES > (SELECT AVG(SALES) * 3 FROM data)
ORDER BY SALES DESC;
```
---

## Rows with Any NULL in Key Columns
**ARGS:** —
**Description:** Flags rows missing values in ORDERNUMBER, SALES, CUSTOMERNAME, or PRODUCTCODE.
```sql
SELECT *
FROM data
WHERE ORDERNUMBER IS NULL
   OR SALES IS NULL
   OR CUSTOMERNAME IS NULL
   OR PRODUCTCODE IS NULL
ORDER BY ORDERNUMBER;
```
---
