# Insights: Overview Numeric Distributions

![overview_numeric_distributions.png](../images/overview_numeric_distributions.png)

## Data Insight
- The 'postalcode' column exhibits a wide range of values, with a dense concentration of lower values and a few outliers extending to nearly 100k. Other numeric columns like 'ordernumber' and 'sales' show much tighter distributions.

## Analysis Insight
- The box plot indicates significant variation in monetary values represented by 'sales' and 'postalcode'. 'Sales' appears to have a more conventional distribution, while 'postalcode' suggests potential data entry issues or a wide geographic spread.

## Caveat
- The 'postalcode' distribution's extreme range might be due to data entry errors or how zip codes are encoded. Without further context, it's difficult to determine if these are genuine values or require cleaning.
