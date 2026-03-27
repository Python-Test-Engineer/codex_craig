# CSV Dataset Report

## Dataset Snapshot
- Rows: 2823
- Columns: 25
- Numeric columns: 10
- Categorical columns: 14
- Date/time columns: orderdate
- Missing cells: 5622

## Numeric Summary
- **ordernumber**: mean=10258.73, std=92.09, min=10100.00, max=10425.00, median=10262.00
- **quantityordered**: mean=35.09, std=9.74, min=6.00, max=97.00, median=35.00
- **priceeach**: mean=83.66, std=20.17, min=26.88, max=100.00, median=95.70
- **orderlinenumber**: mean=6.47, std=4.23, min=1.00, max=18.00, median=6.00
- **sales**: mean=3553.89, std=1841.87, min=482.13, max=14082.80, median=3184.80
- **qtr_id**: mean=2.72, std=1.20, min=1.00, max=4.00, median=3.00
- **month_id**: mean=7.09, std=3.66, min=1.00, max=12.00, median=8.00
- **year_id**: mean=2003.82, std=0.70, min=2003.00, max=2005.00, median=2004.00

## Top Category Distributions
### status (top 5 of 6 unique values)
- Shipped: 2617 (92.7%)
- Cancelled: 60 (2.1%)
- Resolved: 47 (1.7%)
- On Hold: 44 (1.6%)
- In Process: 41 (1.5%)
### productline (top 5 of 7 unique values)
- Classic Cars: 967 (34.3%)
- Vintage Cars: 607 (21.5%)
- Motorcycles: 331 (11.7%)
- Planes: 306 (10.8%)
- Trucks and Buses: 301 (10.7%)
### addressline2 (top 5 of 9 unique values)
- <missing>: 2521 (89.3%)
- Level 3: 55 (1.9%)
- Suite 400: 48 (1.7%)
- Level 6: 46 (1.6%)
- Level 15: 46 (1.6%)
### state (top 5 of 16 unique values)
- <missing>: 1486 (52.6%)
- CA: 416 (14.7%)
- MA: 190 (6.7%)
- NY: 178 (6.3%)
- NSW: 92 (3.3%)
### country (top 5 of 19 unique values)
- USA: 1004 (35.6%)
- Spain: 342 (12.1%)
- France: 314 (11.1%)
- Australia: 185 (6.6%)
- UK: 144 (5.1%)

## Top Correlations
- qtr_id vs month_id: r = 0.979
- ordernumber vs year_id: r = 0.905
- priceeach vs msrp: r = 0.671
- priceeach vs sales: r = 0.658
- sales vs msrp: r = 0.635

## Chart Index
- overview_numeric_distributions.png (overview)
- correlation_heatmap.png (correlation)
- distribution_ordernumber.png (distribution)
- distribution_quantityordered.png (distribution)
- distribution_priceeach.png (distribution)
- distribution_orderlinenumber.png (distribution)
- distribution_sales.png (distribution)
- distribution_qtr_id.png (distribution)
- category_status.png (category)
- category_productline.png (category)
- category_addressline2.png (category)
- category_state.png (category)
- category_country.png (category)
- category_territory.png (category)
- category_dealsize.png (category)
- time_series_ordernumber.png (time)
- time_series_quantityordered.png (time)
- time_series_priceeach.png (time)
- overview_scatter_qtr_id_vs_month_id.png (overview)

## Caveats
- This report is exploratory. Observed patterns should be validated before drawing conclusions.
- Missingness and data quality may influence results.
