# Data Cleaning Log

## 1. Original Dataset

The raw Online Retail dataset (`data/online_retail.csv`) contained **541,909 rows and 8 columns**.

## 2. Duplicate Records

The raw dataset contained **5,268 duplicate rows**. These were removed with `drop_duplicates()` to avoid counting repeated records more than once.

## 3. Missing Values

- **Description:** 1,454 values were missing. These were filled with `Unknown` so the rows could be retained in product-independent analyses.
- **CustomerID:** 135,080 values were missing in the raw dataset. These were retained because the transaction data can still be useful for overall sales analysis. Rows without customer IDs cannot be used reliably for customer-specific analysis.

After cleaning, 135,035 `CustomerID` values remain missing. The count is slightly lower than the raw count because duplicate rows were removed.

## 4. Data Types

`InvoiceDate` was converted from text to datetime in the cleaning script so transactions could be analyzed over time. The cleaned output is CSV, which does not store data types; the EDA script parses `InvoiceDate` as datetime when it reads the file.

## 5. Negative Quantities

Negative quantities were retained because they can represent returns or credit notes. The raw data contained **10,624** negative-quantity rows; **10,587** remain after duplicate removal. Removing them without investigation could distort net sales analysis.

## 6. Unit Prices

- **Zero unit prices:** These were retained for investigation rather than automatically removed. They contribute zero to the `Quantity × UnitPrice` calculation. The raw data had 2,515 zero-price rows; 2,510 remain after duplicate removal.
- **Negative unit prices:** The cleaning script removed **2** rows with negative unit prices. No negative unit prices remain in the cleaned dataset.

## 7. Output

The cleaned dataset was saved as `data/online_retail_cleaned.csv`.

## 8. Validation

The cleaned CSV was checked for row and column counts, missing values, duplicate records, and retained unusual values.

- **Final row count:** 536,639
- **Final column count:** 8
- **Duplicate rows remaining:** 0
- **Missing values remaining:** 135,035, all in `CustomerID`
- **`Description` values filled with `Unknown`:** 1,454
- **Zero unit prices remaining:** 2,510
- **Negative quantities remaining:** 10,587
- **Negative unit prices remaining:** 0

### Notes

The retained missing customer IDs, zero prices, and negative quantities are documented limitations or transaction characteristics, not automatically treated as errors. They should be handled according to the specific analysis: customer-level analysis requires a known `CustomerID`, and net revenue includes the effect of negative quantities.
