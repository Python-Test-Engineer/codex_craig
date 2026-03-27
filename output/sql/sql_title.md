# SQL Query Catalog — sales_data_sample.csv

Dataset: `data/data.csv`
Columns: `ORDERNUMBER`, `QUANTITYORDERED`, `PRICEEACH`, `ORDERLINENUMBER`, `SALES`, `ORDERDATE`, `STATUS`, `QTR_ID`, `MONTH_ID`, `YEAR_ID`, `PRODUCTLINE`, `MSRP`, `PRODUCTCODE`, `CUSTOMERNAME`, `PHONE`, `ADDRESSLINE1`, `ADDRESSLINE2`, `CITY`, `STATE`, `POSTALCODE`, `COUNTRY`, `TERRITORY`, `CONTACTLASTNAME`, `CONTACTFIRSTNAME`, `DEALSIZE`

---

## 1. Overview

1. Total Row Count — Returns the total number of order line items in the dataset.
2. Column Sample — Returns the first 10 rows to preview the full dataset structure.
3. Distinct Value Count per Categorical Column — Shows cardinality for PRODUCTLINE, STATUS, TERRITORY, DEALSIZE, COUNTRY, and CITY.
4. Date Range of Orders — Returns the earliest and latest ORDERDATE in the dataset.
5. Summary Statistics for Key Measures — Returns min, max, avg, and total for SALES, QUANTITYORDERED, and PRICEEACH.

---

## 2. Revenue & Sales

6. Total Sales Revenue — Shows the combined sum of all SALES across the entire dataset.
7. Total Revenue by PRODUCTLINE — Ranks each product line by total SALES generated, highest first.
8. Total Revenue by CUSTOMERNAME — Ranks each customer by total SALES generated, highest first.
9. Total Revenue by COUNTRY — Ranks each country by total SALES generated, highest first.
10. Total Revenue by TERRITORY — Ranks each sales territory (NA, EMEA, APAC, Japan) by total SALES.
11. Total Revenue by CITY — Ranks each city by total SALES, highest first.
12. Total Revenue by DEALSIZE — Compares total SALES across Small, Medium, and Large deal sizes.
13. Total Revenue by PRODUCTCODE — Ranks each product code by total SALES, highest first.
14. Average Revenue per Order Line — Shows the mean SALES value per individual order line.
15. Average PRICEEACH by PRODUCTLINE — Compares average unit selling price across product lines.
16. Revenue by Year — Shows total SALES grouped by YEAR_ID to compare annual performance.
17. Revenue by Quarter — Shows total SALES grouped by QTR_ID to reveal quarterly patterns.

---

## 3. Volume & Orders

18. Total Units Ordered — Shows the sum of QUANTITYORDERED across all order lines.
19. Total Units by PRODUCTLINE — Ranks each product line by total QUANTITYORDERED, highest first.
20. Total Units by CUSTOMERNAME — Ranks each customer by total QUANTITYORDERED, highest first.
21. Total Units by PRODUCTCODE — Ranks each product code by total QUANTITYORDERED, highest first.
22. Total Distinct Order Count — Returns the number of unique ORDERNUMBER values in the dataset.
23. Order Line Count by STATUS — Shows how many order lines fall under each STATUS value.
24. Average Quantity per Order Line — Returns the mean QUANTITYORDERED per line item.
25. Orders with Most Line Items — Ranks orders by number of line items, identifying large complex orders.

---

## 4. Customer Analysis

26. Customers Ranked by Total Revenue — Ranks all customers by lifetime SALES, highest first, with order count.
27. Customers Ranked by Total Units Ordered — Ranks customers by total QUANTITYORDERED, highest first.
28. Customers Ranked by Order Count — Ranks customers by number of distinct orders placed, highest first.
29. Top 5 Customers by Revenue — Lists the 5 highest-revenue customers with total SALES and order count.
30. Bottom 5 Customers by Revenue — Lists the 5 lowest-revenue customers to identify underperformers.
31. Customer Count by COUNTRY — Counts distinct customers per country, ordered by count descending.
32. Customer Count by TERRITORY — Counts distinct customers per territory.
33. Average Revenue per Customer — Returns mean total lifetime SALES across all customers.
34. Repeat vs One-Time Customers — Counts customers with more than one order versus exactly one order.
35. Customers with Total Revenue Above :threshold — Lists customers whose lifetime SALES exceed a given value.

---

## 5. Product Analysis

36. Products Ranked by Total Revenue — Ranks each PRODUCTCODE by total SALES, highest first.
37. Products Ranked by Total Units Sold — Ranks each PRODUCTCODE by total QUANTITYORDERED, highest first.
38. Top 5 Products by Revenue — Lists the 5 highest-revenue products with total sales and units.
39. Bottom 5 Products by Revenue — Lists the 5 lowest-revenue products to identify slow sellers.
40. Top 3 Products by Revenue — Lists the 3 highest-revenue products for quick-reference ranking.
41. Top 10 Products by Revenue — Lists the 10 highest-revenue products for broader analysis.
42. Product Lines Ranked by Total Revenue — Ranks product lines by total SALES with units and order count.
43. Product Lines Ranked by Total Units Sold — Ranks product lines by total QUANTITYORDERED, highest first.
44. Average PRICEEACH vs MSRP by PRODUCTCODE — Compares average actual selling price against MSRP to reveal discount per product.
45. Products Selling Below MSRP on Average — Flags products where average PRICEEACH is less than MSRP.

---

## 6. Territory & Country Analysis

46. Countries Ranked by Total Revenue — Ranks each country by total SALES, highest first.
47. Countries Ranked by Total Units Ordered — Ranks each country by total QUANTITYORDERED, highest first.
48. Territories Ranked by Total Revenue — Ranks NA, EMEA, APAC, Japan by total SALES.
49. Revenue by Territory and Country — Shows total SALES for each country grouped within its territory.
50. Cities Ranked by Total Revenue — Ranks cities by total SALES, highest first.
51. Top 5 Countries by Revenue — Lists the 5 highest-revenue countries with total SALES.
52. Bottom 5 Countries by Revenue — Lists the 5 lowest-revenue countries to identify weak markets.
53. Customer Count and Revenue by Territory — Shows distinct customer count and total SALES per territory.

---

## 7. Time-Based Analysis

54. Monthly Revenue Trend — Returns total SALES grouped by year-month, ordered chronologically.
55. Yearly Revenue Total — Shows total SALES per YEAR_ID to compare 2003, 2004, and 2005.
56. Quarterly Revenue by Year — Shows SALES per quarter per year to reveal seasonal patterns.
57. Monthly Revenue by PRODUCTLINE — Shows monthly SALES trend broken down by product line.
58. Best Month by Revenue — Identifies the single year-month with the highest total SALES.
59. Revenue Between :start_date and :end_date — Returns total SALES within an arbitrary date range.
60. Transactions Between :start_date and :end_date — Returns all order lines within a specified date range.
61. Revenue for :year — Returns total SALES for a specific four-digit year.
62. Revenue for :year_month — Returns total SALES for a specific month in YYYY-MM format.
63. Month-over-Month Revenue Change — Compares each month's total SALES against the prior month using self-join.

---

## 8. Status & Deal Size Analysis

64. Revenue by STATUS — Shows total SALES grouped by order STATUS (Shipped, Disputed, Cancelled, etc.).
65. Order Count by STATUS — Counts order lines per STATUS to show order pipeline distribution.
66. Disputed Orders by CUSTOMERNAME — Lists customers with Disputed status orders and their total disputed SALES.
67. Revenue by DEALSIZE — Shows total SALES, order count, and avg SALES per deal size category.
68. DEALSIZE Distribution by PRODUCTLINE — Shows count of Small, Medium, Large deals for each product line.
69. Cancelled or On Hold Orders — Returns all order lines with STATUS = 'Cancelled' or 'On Hold'.

---

## 9. Parametric Lookups

70. All Transactions for CUSTOMERNAME = :customer_name — Returns all order lines for a specific customer ordered by date.
71. Revenue Summary for CUSTOMERNAME = :customer_name — Returns total SALES, orders, and units for one specific customer.
72. Full Performance for CUSTOMERNAME = :customer_name — Shows SALES, units, avg price, and order count for one customer.
73. Top Products for CUSTOMERNAME = :customer_name — Ranks products by SALES for one specific customer.
74. Monthly Revenue Trend for CUSTOMERNAME = :customer_name — Shows monthly SALES trend for one customer.
75. All Transactions for PRODUCTCODE = :product_code — Returns all order lines for a specific product code.
76. Revenue Summary for PRODUCTCODE = :product_code — Returns total SALES, units, and avg price for one product.
77. Top Customers for PRODUCTCODE = :product_code — Ranks customers by SALES for a specific product code.
78. All Transactions for COUNTRY = :country — Returns all order lines for a specific country ordered by date.
79. Revenue Summary for COUNTRY = :country — Returns total SALES, order count, and units for one country.
80. Revenue and Orders for PRODUCTLINE = :product_line — Returns total SALES, units, and order count for one product line.
81. Revenue Summary for TERRITORY = :territory — Returns total SALES, customer count, and units for one territory.
82. Revenue and Orders for DEALSIZE = :deal_size — Returns total SALES and order count for a specific deal size.
83. Orders Above :min_revenue — Returns all order lines where SALES exceed a given minimum threshold.
84. Revenue for CUSTOMERNAME = :customer_name in COUNTRY = :country — Returns SALES filtered to a specific customer-country combination.

---

## 10. Advanced Analytics

85. Revenue Share % by PRODUCTLINE — Shows each product line's SALES as a percentage of the grand total.
86. Revenue Share % by CUSTOMERNAME — Shows each customer's SALES contribution as a percentage of total revenue.
87. Revenue Share % by COUNTRY — Shows each country's SALES as a percentage of the grand total.
88. Cumulative Revenue Over Time — Shows running total of SALES ordered chronologically using self-join.
89. Customer Revenue vs Dataset Average — Compares each customer's total SALES against the overall dataset average.
90. Product Revenue as % of PRODUCTLINE Total — Shows each product's SALES share within its own product line.
91. Average Order Value by CUSTOMERNAME — Shows average SALES per distinct order for each customer.
92. Pareto: Customers Generating Top 80% of Revenue — Identifies the high-value customer segment using CTE and running sum.

---

## 11. Data Quality Checks

93. NULL Count per Column — Counts NULL values in each column, ordered by count descending.
94. Duplicate ORDERNUMBER + ORDERLINENUMBER Combinations — Flags any order line combinations that appear more than once.
95. Negative SALES Values — Flags rows where SALES is negative, indicating potential data entry errors.
96. Negative QUANTITYORDERED Values — Flags rows where QUANTITYORDERED is less than zero.
97. SALES Calculation Validation — Flags rows where SALES differs from QUANTITYORDERED × PRICEEACH by more than 1.
98. Price Below MSRP Check — Lists products where average PRICEEACH is less than MSRP, showing discount magnitude.
99. Outlier SALES Rows — Returns rows where SALES is more than 3 times the dataset average.
100. Rows with Any NULL in Key Columns — Flags rows missing values in ORDERNUMBER, SALES, CUSTOMERNAME, or PRODUCTCODE.

---

*Generated from dataset inspection — sales order dataset with 25 columns covering 2003–2005 transactions across products, customers, countries, and territories*
