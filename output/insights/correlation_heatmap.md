# Insights: Correlation Heatmap

![correlation_heatmap.png](../images/correlation_heatmap.png)

## Data Insight
- The heatmap shows strong positive correlations among financial metrics: total_cost correlates strongly with total_revenue (r>0.9), profit correlates with both revenue and margin_pct. Unit_price and unit_cost display moderate positive correlation. Quantity shows weak correlation with total_cost, indicating unit values drive total costs more than volume.

## Analysis Insight
- Cost and price variables cluster together, reflecting consistent markup behavior. The margin_pct metric behaves independently from quantity-based variables, suggesting margin is determined by product pricing rather than purchase volume. Weak correlations with encoded categorical variables (customer_id, store_id) indicate limited segment-specific financial patterns in this 100-row sample.

## Caveat
- Correlation does not imply causation; relationships may be definitional (total_revenue = unit_price × quantity). Categorical variables appear encoded numerically, inflating some correlations. The small sample size (n=100) limits generalizability, and time-based dependencies in the date variable are not captured in pairwise correlations.
