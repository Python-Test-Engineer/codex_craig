# Insights: Correlation Heatmap

![correlation_heatmap.png](../images/correlation_heatmap.png)

## Data Insight
- The heatmap shows a strong positive correlation of 0.94 between unit_price and total_price, and a weak positive correlation of 0.26 between quantity and total_price. Unit_price and quantity have a near-zero correlation (0.02).

## Analysis Insight
- Total price is strongly influenced by unit price, suggesting that higher-priced items contribute more to the total cost. The weak correlation with quantity indicates that the number of items sold might have a less significant impact on total price compared to individual item costs.

## Caveat
- The low number of rows (20) limits the statistical significance and generalizability of these correlation findings. Other unobserved factors ('city', 'date', 'product_name') could confound these relationships.
