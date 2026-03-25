# Insights: Distribution Total Cost

![distribution_total_cost.png](../images/distribution_total_cost.png)

## Data Insight
- The total_cost distribution shows strong right-skewness with mean=1341.73 and std=1753.29. Most orders cluster at lower cost levels while a minority generate substantially higher costs, creating a long tail. The standard deviation exceeding the mean indicates high variability across orders.

## Analysis Insight
- The skewed distribution suggests a small proportion of orders drive disproportionate cost volume. High coefficient of variation (~131%) implies heterogeneous order profiles. This pattern is typical in transactional datasets where bulk or premium orders inflate variance.

## Caveat
- Without visualizing the actual histogram or density plot, distribution shape is inferred from summary statistics. Outlier influence on the mean cannot be confirmed without viewing individual data points or quartile values.
