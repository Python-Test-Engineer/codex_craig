# Insights: Distribution Total Revenue

![distribution_total_revenue.png](../images/distribution_total_revenue.png)

## Data Insight
- The total revenue distribution is likely right-skewed with most orders generating moderate revenue and a few high-value orders driving the upper tail. Given unit_price mean of $376.69 and quantity mean of 6.12, average transaction revenue approximates $2,305, with substantial variation implied by the high standard deviations in unit cost and unit price.

## Analysis Insight
- The wide gap between unit_cost (mean $219.84) and unit_price (mean $376.69) indicates consistent markup across products. With total_cost averaging $1,341.73 per order, the profit distribution likely mirrors revenue distribution patterns, reflecting the multiplicative relationship between price, quantity, and revenue.

## Caveat
- Without total_revenue statistics explicitly provided, conclusions rely on derived estimates from component columns. The small sample size of 100 orders limits generalizability, and revenue distribution shape cannot be confirmed without visualization inspection.
