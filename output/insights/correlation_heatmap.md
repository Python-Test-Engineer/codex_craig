# Insights: Correlation Heatmap

![correlation_heatmap.png](../images/correlation_heatmap.png)

## Data Insight
- Sales show a strong positive correlation with quantity ordered (0.55) and price each (0.66). Order number is highly correlated with year (0.90), indicating a potential increase in order volume over time. Quarter and month IDs are strongly correlated (0.98), as expected.

## Analysis Insight
- The heatmap reveals significant positive correlations between sales and both quantity ordered and price each. The strong correlation between order number and year suggests a growing customer base or order frequency. Quartile and month IDs exhibit very high correlation, as they are intrinsically linked.

## Caveat
- These correlations do not imply causation. Other factors not present in this heatmap (e.g., marketing campaigns, economic conditions) could influence sales. The 'year_id' correlation might be influenced by the specific time period covered by the data.
