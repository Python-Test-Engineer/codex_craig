# Insights: Distribution Profit

![distribution_profit.png](../images/distribution_profit.png)

## Data Insight
- The profit distribution appears right-skewed with most transactions generating modest profits while a smaller subset yields substantially higher returns. Unit cost and unit price show high variability (std 241.86 and 358.32 respectively) relative to their means, indicating diverse product pricing. Average quantity per order is 6.05 units with moderate consistency (std 3.01).

## Analysis Insight
- Transaction-level profit likely varies considerably across stores or product categories given the wide dispersion in cost and price metrics. The high standard deviation in total_cost (1764.62) relative to its mean (1206.41) suggests significant heterogeneity in order sizes, potentially driven by product type or store location differences visible in the chart's distribution patterns.

## Caveat
- Interpretation is limited without seeing actual profit values or chart axes; aggregation may mask individual transaction outliers. Store-level or product-level confounding could explain apparent patterns. The 39-row sample may not generalize to broader operational periods, and temporal effects remain unexamined.
