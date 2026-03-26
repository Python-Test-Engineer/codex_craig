# CSV Dataset Report

## Dataset Snapshot
- Rows: 39
- Columns: 17
- Numeric columns: 7
- Categorical columns: 9
- Date/time columns: date
- Missing cells: 0

## Numeric Summary
- **unit_cost**: mean=198.42, std=241.86, min=8.50, max=650.00, median=55.00
- **unit_price**: mean=344.86, std=358.32, min=29.99, max=999.99, median=149.99
- **quantity**: mean=6.05, std=3.01, min=1.00, max=10.00, median=7.00
- **total_cost**: mean=1206.41, std=1764.62, min=17.00, max=6500.00, median=360.00
- **total_revenue**: mean=2096.09, std=2674.36, min=59.98, max=9999.90, median=799.90
- **profit**: mean=889.68, std=928.13, min=42.98, max=3499.90, median=474.95
- **margin_pct**: mean=55.21, std=13.32, min=35.00, max=71.70, median=63.30

## Top Category Distributions
### customer_id (top 5 of 10 unique values)
- C02: 10 (25.6%)
- C04: 5 (12.8%)
- C05: 5 (12.8%)
- C09: 4 (10.3%)
- C06: 3 (7.7%)
### customer_name (top 5 of 10 unique values)
- Bob Smith: 10 (25.6%)
- David Brown: 5 (12.8%)
- Emma Davis: 5 (12.8%)
- Isabella Taylor: 4 (10.3%)
- Frank Miller: 3 (7.7%)
### product_id (top 5 of 5 unique values)
- P004: 11 (28.2%)
- P003: 8 (20.5%)
- P001: 8 (20.5%)
- P002: 7 (17.9%)
- P005: 5 (12.8%)
### product_name (top 5 of 6 unique values)
- Monitor: 11 (28.2%)
- Keyboard: 8 (20.5%)
- Laptop: 8 (20.5%)
- Mouse: 6 (15.4%)
- Headphones: 5 (12.8%)
### store_id (top 3 of 3 unique values)
- S2: 14 (35.9%)
- S1: 13 (33.3%)
- S3: 12 (30.8%)

## Top Correlations
- unit_cost vs unit_price: r = 0.998
- total_cost vs total_revenue: r = 0.996
- total_revenue vs profit: r = 0.987
- total_cost vs profit: r = 0.970
- unit_price vs margin_pct: r = -0.944

## Chart Index
- overview_numeric_distributions.png (overview)
- correlation_heatmap.png (correlation)
- distribution_unit_cost.png (distribution)
- distribution_unit_price.png (distribution)
- distribution_quantity.png (distribution)
- distribution_total_cost.png (distribution)
- distribution_total_revenue.png (distribution)
- distribution_profit.png (distribution)
- category_order_id.png (category)
- category_customer_id.png (category)
- category_customer_name.png (category)
- category_product_id.png (category)
- category_product_name.png (category)
- category_store_id.png (category)
- category_store_name.png (category)
- category_city.png (category)
- time_series_unit_cost.png (time)
- time_series_unit_price.png (time)
- time_series_quantity.png (time)
- overview_scatter_unit_cost_vs_unit_price.png (overview)

## Caveats
- This report is exploratory. Observed patterns should be validated before drawing conclusions.
- Missingness and data quality may influence results.
