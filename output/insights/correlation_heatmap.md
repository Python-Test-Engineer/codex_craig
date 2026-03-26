# Insights: Correlation Heatmap

![correlation_heatmap.png](../images/correlation_heatmap.png)

## Data Insight
- The heatmap displays Pearson correlation coefficients between numeric variables. Cost and revenue variables (total_cost, total_revenue, profit) show strong positive correlations (r>0.7). Quantity correlates positively with total_cost and total_revenue but weakly with margin_pct. Unit_price and unit_cost display moderate correlation, indicating related pricing and costing structures.

## Analysis Insight
- Strong correlations among total_cost, total_revenue, and profit reflect the inherent accounting relationships in sales data where revenue minus cost determines profit. The weak correlation between margin_pct and quantity suggests no clear volume discount pattern. Store-level and payment_method variables likely show minimal correlation with financial metrics due to their categorical nature.

## Caveat
- Correlation does not imply causation; relationships may be confounded by product type or store effects. The small sample size (n=39) limits statistical power and precision of correlation estimates. Missing data handling and outlier presence were not disclosed, which could distort correlation values.
