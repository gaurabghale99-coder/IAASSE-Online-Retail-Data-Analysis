# Week 3: Exploratory Data Analysis (EDA)

## 1. Data Overview

- **Number of rows and columns:** The cleaned dataset contains 536,639 rows and 8 original columns. I added a `Revenue` column, calculated as `Quantity multiplied by UnitPrice`, and a derived month field for trend analysis.
- **Date range:** December 1, 2010, at 08:26 to December 9, 2011, at 12:50.
- **Important numerical columns:**
  - `Quantity`: Number of units recorded on an invoice line.
  - `UnitPrice`: Price per unit.
  - `Revenue`: Value of an invoice line, calculated by multiplying quantity by unit price. Negative quantities produce negative revenue.

## 2. Distribution Analysis

- **Quantity distribution:** The median quantity is 3, the 75th percentile is 10, and the mean is 9.62. Most invoice lines contain relatively small quantities. However, the dataset includes extreme positive and negative values, ranging from -80,995 to 80,995. The skewness is slightly negative (-0.26), influenced by extreme negative values, even though positive quantities also have a long upper tail.
- **UnitPrice distribution:** The median unit price is 2.08, and the 75th percentile is 4.13. The maximum price is 38,970, resulting in strong right skewness (205.82). This means most prices are relatively low, while a small number of records have extremely high prices.
- **Interpretation:** Extreme values can pull the mean away from the typical value. Therefore, the median and percentiles are useful for understanding typical quantities and prices.

## 3. Correlation Analysis

The Pearson correlation coefficients were calculated using the retained records, including negative quantities and zero prices.

- **Quantity and UnitPrice (-0.001):** There is virtually no linear relationship between quantity and unit price.
- **Quantity and Revenue (0.888):** There is a strong positive linear relationship. Larger quantities generally correspond to higher revenue, although the relationship is also affected by unit prices and returns.
- **UnitPrice and Revenue (-0.179):** There is a weak negative linear relationship in this dataset. This does not mean higher prices cause lower revenue. Returns, zero-priced transactions, and extreme values may influence the result.
- **Interpretation:** Correlation measures the strength and direction of a linear relationship between two variables. It does not establish cause and effect.

## 4. Trend Analysis

- **Highest monthly net recorded revenue:** November 2011, with net recorded revenue of 1,456,145.80.
- **Lowest monthly net recorded revenue:** December 2011, with net recorded revenue of 432,701.06. However, the dataset contains records only through December 9, making it an incomplete month.
- **Lowest net recorded revenue among complete months:** April 2011, with net recorded revenue of 492,367.84.
- **Monthly net recorded revenue pattern:** Net recorded revenue fluctuated throughout the period and increased strongly from September through November 2011, reaching its highest level in November. December's lower total is partly explained by incomplete data.
- **Monthly invoice volume:** The number of unique invoices increased from 1,393 in February 2011 to 3,462 in November 2011, although some monthly decreases occurred. December had 1,015 invoices through December 9 and is also incomplete.

**Interpretation:** The monthly chart sums `Quantity × UnitPrice` across all invoice lines. Its totals are **net recorded revenue**: positive recorded sales are offset by negative recorded transactions, which may represent returns or credit notes. For example, £60 of positive recorded sales and -£10 of negative transactions produce £50 net recorded revenue. These totals should not be described as positive sales alone, and the reason for a negative transaction should not be assumed without checking it. November had the highest net recorded revenue and invoice volume, while comparisons involving December should account for its shorter observation period.

## 5. Product Analysis

The following table shows the top 10 products by net quantity sold. Net quantity is the sum of recorded quantities, so negative quantities from returns or cancellations reduce the total.

| Rank | Product | Net quantity |
|---:|--- |---:|
| 1 | WORLD WAR 2 GLIDERS ASSTD DESIGNS | 53,751 |
| 2 | JUMBO BAG RED RETROSPOT | 47,260 |
| 3 | POPCORN HOLDER | 36,322 |
| 4 | ASSORTED COLOUR BIRD ORNAMENT | 36,282 |
| 5 | PACK OF 72 RETROSPOT CAKE CASES | 36,016 |
| 6 | WHITE HANGING HEART T-LIGHT HOLDER | 35,298 |
| 7 | RABBIT NIGHT LIGHT | 30,631 |
| 8 | MINI PAINT SET VINTAGE | 26,437 |
| 9 | PACK OF 12 LONDON TISSUES | 26,299 |
| 10 | PACK OF 60 PINK PAISLEY CAKE CASES | 24,719 |

**Interpretation:** The leading products include novelty, gift, and household items. This ranking measures net units, not revenue or the number of orders. Product descriptions were used to group the records.

## 6. Anomaly Analysis

- **Negative quantities:** 10,587 records contain negative quantities. These commonly represent returns or cancellations, although individual records should be checked before assigning a definitive reason.
- **Zero or negative unit prices:** 2,510 records have zero prices, and no records have negative prices in the cleaned dataset. Zero-priced items may represent samples, promotions, or adjustments and should be investigated.
- **Quantity outliers (IQR method):** 58,501 records were flagged using lower and upper bounds of -12.5 and 23.5. Of these, 1,976 were below the lower bound and 56,525 were above the upper bound.
- **UnitPrice outliers (IQR method):** 39,448 records were flagged using bounds of -3.07 and 8.45. All were above the upper bound, with none below the lower bound.
- **Interpretation and handling decisions:** The IQR method identifies statistically unusual values, not necessarily incorrect records. Negative quantities can be retained for net sales analysis, while completed-sales analysis may require separate treatment of returns. Zero-priced records should be investigated before removal. Valid high-volume and high-price transactions should not be deleted automatically. Extreme records should be inspected, and any filtering should be documented.

## 7. Conclusion

The cleaned online retail dataset contains 536,639 invoice lines covering just over a year. Most quantities and unit prices are relatively small, but both distributions contain extreme values, particularly unit prices. Quantity and revenue have a strong positive correlation, while quantity and unit price have virtually no linear correlation. Monthly net recorded revenue and invoice volume generally increased toward autumn 2011, with November recording the highest totals. Monthly net recorded revenue includes negative transactions, which may represent returns or credit notes; December is incomplete and requires careful interpretation. The leading products are mainly novelty, gift, and household items. Negative quantities, zero prices, and IQR outliers should be investigated and handled according to the analysis objective rather than removed automatically.

## Business Recommendations

### 1. Improve Seasonal Inventory Planning

November had the highest monthly net recorded revenue and invoice volume in this dataset. Review the November peak alongside the top-products chart and use product-level demand to inform stock planning for busy periods. The revenue figure is net of negative transactions, which may include returns or credit notes. The dataset covers only a little over one year, so compare with additional years before treating this as a recurring seasonal pattern.

### 2. Make Fair December Comparisons

The dataset ends on December 9, 2011, so the December net recorded revenue and invoice totals cover only part of the month. Compare the first nine days of December with the first nine days of other months or years, or exclude December from full-month comparisons.

### 3. Investigate Returns and Zero-Priced Transactions

The analysis identified negative-quantity records and zero-unit-price transactions. Review these transactions to understand returns, cancellations, credit notes, samples, or adjustments before making operational decisions. When reporting performance, show positive recorded sales, negative transactions, and net recorded revenue separately where possible. The monthly chart keeps the transaction-level `Quantity × UnitPrice` calculation and sums all lines, so negative quantities reduce the net total.

## Limitations

- The dataset covers a little over one year, which is insufficient to establish a recurring seasonal pattern.
- December 2011 contains data only through December 9, so its total is not comparable with complete months.
- The analysis shows patterns and associations but does not establish why sales changed or whether a promotion caused a change.
- Historical patterns in this dataset alone cannot establish whether sales patterns will repeat in the future.
- Missing `CustomerID` values limit customer-specific analysis, while retained negative quantities and zero-priced transactions require context when interpreting sales totals.
