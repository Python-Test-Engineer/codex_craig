# Insights: Overview Numeric Distributions

![overview_numeric_distributions.png](../images/overview_numeric_distributions.png)

## Data Insight
- The numeric variables show right-skewed distributions typical of sales data. Unit cost and unit price have high standard deviations relative to their means (std/mean ratios of 1.22 and 1.04 respectively), indicating substantial variability with a long tail of high-value transactions. Quantity is more normally distributed with a lower coefficient of variation (0.50), clustering around the mean of 6 units per order.

## Analysis Insight
- Total cost exhibits the largest absolute dispersion (std=1764.62) driven by the multiplicative effect of quantity and unit cost. The margin between unit price and unit cost (mean spread of ~146) suggests consistent profitability per unit, though profit distribution likely mirrors the right-skew of revenue-generating transactions. Outliers in unit price and total cost likely represent bulk orders or premium product purchases.

## Caveat
- Distribution shapes are inferred from summary statistics without access to raw data points or visualization. The small sample size (n=39) limits statistical power and may not represent broader population patterns. Standard deviation estimates are themselves uncertain with limited observations.
