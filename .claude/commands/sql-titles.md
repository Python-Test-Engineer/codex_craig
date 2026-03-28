---
description: "Examine a CSV and generate a categorised list of useful SQL query titles in natural language. Usage: /sql-titles [csv_file]"
allowed-tools: Read, Glob, Grep, Write, Bash
argument-hint: "data/data.csv"
---

Parse `$ARGUMENTS`:
- `CSV_FILE` — first token (path to the CSV file)

If missing or empty: check `output/sql/original_csv.md` — if it exists, read it to get the last-uploaded filename and resolve it as `data/<filename>`. If that file does not exist either, fall back to `data/data.csv`. If `data/data.csv` does not exist, glob `data/*.csv`, list available files, and ask the user to pick one.

---

## Your role

You are a senior data analyst. Your job is to examine a CSV dataset and produce a
comprehensive, categorised catalog of useful SQL query titles — each paired with a concise
description that tells `/sql-create` exactly what SQL to generate and tells a user exactly
what question the query answers.

---

## Step 1 — Read the CSV

Read `CSV_FILE` using the Read tool.

Extract:
- **Column names** and their inferred data types (numeric, text, date, id, etc.)
- **Distinct values** for low-cardinality columns (categories, statuses, names, payment methods, etc.)
  — scan the first 100–200 rows to identify them
- **Date range** if a date column is present
- **Key entities** — what are the main dimensions? (products, customers, stores, regions, etc.)
- **Key measures** — what numeric columns exist? (revenue, profit, quantity, cost, margin, etc.)

Note any obvious **data quality issues** visible in the sample:
- Missing or null values in key columns
- Duplicate IDs
- Negative values in quantity/amount columns
- Apparent typos in category names

---

## Step 2 — Design the query catalog

Based on the columns and data discovered in Step 1, design a comprehensive set of SQL query
titles organised into thematic sections. **Aim for 80–100 query titles total.**

Think like an experienced SQL Administrator being examined in a technical interview — cover
every angle: aggregations, rankings, parametric lookups, cross-dimensional breakdowns,
time-series, advanced analytics, and data quality. Leave no obvious question unanswered.

---

### Standard analytical sections

Always include these sections if supported by the data:

1. **Overview** — row count, column sample, distinct value counts per key column
2. **Revenue & Sales** — grand total, by each dimension (product/customer/store/region), averages, per-unit
3. **Volume & Orders** — transaction counts, units sold, average order size, order frequency
4. **Profit & Margin** — profit totals, average margin, margin by dimension, margin distribution
5. **Customer Analysis** — top customers by revenue/profit/orders, frequency, recency, avg spend (if customer data)
6. **Product Analysis** — bestsellers by revenue/units/profit, slowest sellers, unit economics, price vs cost (if product data)
7. **[Entity] Analysis** — one section per additional key entity (store, region, channel, etc.)
8. **Time-Based Analysis** — monthly/yearly trends, period-over-period comparison, seasonality (if date col)
9. **[Category] Analysis** — one section per remaining categorical dimension (payment method, status, tier, etc.)
10. **Data Quality Checks** — NULL counts, duplicates, negative values, referential integrity, calculation consistency

---

### Mandatory ranking queries

For **every key dimension** (product, customer, store, region, etc.) generate all of:

- **[Dimension] Ranked by Total Revenue** — `SUM(revenue)` per dimension, DESC, with transaction count + avg margin
- **[Dimension] Ranked by Total Profit** — `SUM(profit)` per dimension, DESC
- **[Dimension] Ranked by Total Units Sold** — `SUM(quantity)` per dimension, DESC
- **Top 5 [Dimension] by Revenue** — `LIMIT 5`, DESC — quick "who's #1" answer
- **Bottom 5 [Dimension] by Revenue** — `LIMIT 5`, ASC — identifies underperformers

---

### Mandatory parametric queries (comprehensive)

For **every key categorical dimension** generate ALL of the following. Use named placeholders
(`:param_name`). These are the most valuable queries for Ask AI — anticipate every entity-
specific question a business user could ask.

**Per single dimension (repeat for each: customer, product, store, city, payment method, etc.):**

- **All Transactions for [Dimension] = :param** — `SELECT * WHERE dim = :param ORDER BY date`
- **Revenue Summary for [Dimension] = :param** — total revenue, orders, units, avg order value for one value
- **Full Performance for [Dimension] = :param** — revenue, profit, units, avg margin, order count for one value
- **Monthly Revenue Trend for [Dimension] = :param** — revenue grouped by month for one entity (if date col)
- **Top Products Bought by [Customer] = :param** — revenue/units by product filtered to one customer
- **Top Customers for [Product] = :param** — revenue/units by customer filtered to one product
- **[Dimension] Comparison: :param vs dataset average** — entity's metrics vs overall avg (use subquery or CTE)

**Cross-dimensional parametric (at least one per dimension pair):**

- **Revenue for [Dim1] = :d1 and [Dim2] = :d2** — filtered to specific combination of two dimensions
- **[Dim2] Breakdown for [Dim1] = :param** — aggregate Dim2 values filtered to one Dim1 value
- **[Dim1] Performance in [Store/Region] = :param** — product/customer metrics filtered to one location

**Date-parametric (if date column present):**

- **Revenue Between :start_date and :end_date** — total revenue in arbitrary date range
- **Transactions Between :start_date and :end_date** — all rows in date range
- **[Dimension] Performance Between :start_date and :end_date** — dimension breakdown in date range
- **Revenue for :year** — total revenue for a specific year (`:year` as 4-digit string)
- **Revenue for :year_month** — total revenue for a specific month (`:year_month` as `YYYY-MM`)

**Threshold / comparison parametric:**

- **Orders Above :min_revenue** — transactions where revenue exceeds a given threshold
- **Customers with Total Revenue Above :threshold** — customers whose lifetime spend exceeds threshold
- **Products with Margin Below :min_margin** — flags low-margin products below a threshold
- **Top :n Products by Revenue** — parameterised N (note: SQLite doesn't support `:n` in LIMIT, so use a fixed set of top-N queries: top 3, 5, 10)

---

### Advanced analytics queries

Include these if the data supports them (they distinguish a strong SQL skill set):

- **Revenue Share % by [Dimension]** — each dimension's revenue as percentage of grand total (subquery)
- **Cumulative Revenue Over Time** — running total of revenue ordered by date (window function or self-join)
- **Month-over-Month Revenue Change** — revenue this month vs prior month as % change (LAG or self-join)
- **[Dimension] Revenue as % of Category Total** — e.g. each product's revenue share within its category
- **Average Order Value by [Dimension]** — `SUM(revenue) / COUNT(DISTINCT order_id)` per dimension
- **Revenue per Transaction by [Dimension]** — avg revenue per row grouped by dimension
- **Pareto: Customers Generating Top 80% of Revenue** — identify high-value customer segment (CTE + running sum)
- **Products Never Ordered Together** — products with no overlap in customer base (if order detail data)
- **Repeat vs One-Time [Customers]** — count customers with >1 order vs exactly 1 (if order ID present)
- **[Dimension] Contribution to Total Profit** — profit contribution % and rank for each dimension value

---

### Data quality deep-dive queries

Go beyond basic NULL counts — an experienced DBA would also check:

- **NULL Count per Column** — counts NULLs in every column, ordered by severity
- **Duplicate [ID] Values** — finds any primary key appearing more than once
- **Negative [Metric] Values** — flags rows where quantity/cost/revenue is negative
- **[Revenue] Calculation Validation** — checks if `quantity × unit_price ≈ total_revenue` (within rounding)
- **[Cost] Calculation Validation** — checks if `quantity × unit_cost ≈ total_cost`
- **Margin Consistency Check** — flags rows where `(revenue - cost) / revenue` differs from stored margin_pct
- **Price Below Cost (Loss-Making Rows)** — rows where `unit_price < unit_cost`
- **Outlier [Revenue] Rows** — rows where revenue is more than 3× the average (potential data entry errors)
- **[ID] Without Matching [FK]** — orphaned records where a foreign key has no matching parent
- **Distinct Value Count per Categorical Column** — cardinality of every text column
- **Typo Detection in [Category]** — groups similar-looking category values (e.g. "Mousse" vs "Mouse")
- **Rows with Any NULL** — flags any row containing at least one NULL in key columns

---

Tailor every title and section name to the actual columns and entities in this dataset.
Use real column names, real entity names (product names, store names, etc.) in titles where helpful.
Do not use generic placeholders — if the dimension is `store_name`, say `store_name`, not `[Dimension]`.

---

## Step 3 — Write `sql_title.md`

Save the catalog to:

```
output/sql/sql_title.md
```

### Entry format

Each query title must be followed immediately by a description on the same line, separated
by ` — ` (space–em-dash–space):

```
N. <Query title> — <Description>
```

**Description rules** (these flow directly into `/sql-create` as the `**Description:**` field):
- One sentence, max 20 words
- Start with a verb: `Shows`, `Returns`, `Ranks`, `Identifies`, `Compares`, `Flags`, `Lists`
- Name the specific metric **and** dimension — not just "revenue" but "total revenue per product"
- Be distinct enough that Claude can select the right query from a user's natural-language question

Good examples:
```
1. Total Sales Revenue — Shows the combined sum of all order revenue across the entire dataset.
2. Total Revenue by Product — Ranks each product by total revenue generated, highest first.
3. Duplicate Order IDs — Flags any order_id that appears more than once in the dataset.
4. Average Unit Price vs Unit Cost by Product — Compares average selling price against cost to show per-product unit margin.
```

### Full file structure

```markdown
# SQL Query Catalog — <csv_filename>

Dataset: `<CSV_FILE>`
Columns: `col1`, `col2`, `col3`, ...

---

## 1. <Section Name>

1. <Query title> — <Description>
2. <Query title> — <Description>
...

---

## 2. <Section Name>

N. <Query title> — <Description>
...

---

*Generated from dataset inspection — <brief one-line summary of dataset scope>*
```

Number queries **continuously** across all sections (do not restart at 1 per section).

---

## Step 4 — Confirm

Tell the user:
- Total number of query titles written
- Sections included
- Path to the output file (`output/sql/sql_title.md`)
- Count of parametric queries (those with `:param` placeholders)
- Any data quality issues spotted during inspection