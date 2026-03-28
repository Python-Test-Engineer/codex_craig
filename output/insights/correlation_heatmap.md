# Insights: Correlation Heatmap

![correlation_heatmap.png](../images/correlation_heatmap.png)

## Data Insight
- The heatmap shows a very strong positive correlation (0.94) between 'unit_price' and 'total_price'. 'Quantity' shows a negligible correlation with both 'unit_price' (0.02) and 'total_price' (0.26).

## Analysis Insight
- The high correlation between 'unit_price' and 'total_price' suggests that the total price is largely driven by the unit price of products sold. The low correlation with quantity indicates that the number of items bought doesn't significantly affect the total sale value in this dataset.

## Caveat
- The analysis is based on a small dataset (20 rows), and correlations observed may not represent the general trend. Other factors influencing total price, not included in the chart, could be significant.
