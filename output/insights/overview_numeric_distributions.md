# Insights: Overview Numeric Distributions

![overview_numeric_distributions.png](../images/overview_numeric_distributions.png)

## Data Insight
- The chart displays distributions for unit_cost, unit_price, quantity, and total_cost. Unit_cost shows right-skewed distribution with mean 219.84 and high dispersion (std=252.72). Unit_price exhibits similar positive skew (mean=376.69, std=370.50). Quantity distribution appears more concentrated around mean 6.12 with lower spread (std=2.88). Total_cost shows the widest range with mean 1341.73 and largest standard deviation (1753.29).

## Analysis Insight
- The high standard deviations relative to means for unit_cost, unit_price, and total_cost indicate substantial variability in transaction values. Quantity's tighter distribution suggests more consistent order sizes. The right-skewed patterns imply a majority of transactions involve lower-valued products, with occasional high-value outliers driving up means. Total_cost variability likely combines effects of quantity and unit_price variation.

## Caveat
- Distribution details depend on binning choices and chart type used. The 100-row sample may not represent broader patterns. Outlier handling and measurement scale assumptions affect observed distributions. Confounding factors like product category, store, or time period are not controlled in this univariate view.
