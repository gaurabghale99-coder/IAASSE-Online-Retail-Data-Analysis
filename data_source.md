# Dataset Source Documentation

## Dataset Name

Online Retail Dataset (also known as E-Commerce Data on Kaggle).

## Source

- **Original source:** [UCI Machine Learning Repository — Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Kaggle page:** [E-Commerce Data by Carrie](https://www.kaggle.com/datasets/carrie1/ecommerce-data)
- **Local raw dataset:** `data/online_retail.csv`

The dataset originates from the UCI Machine Learning Repository. The Kaggle version provides another way to access the dataset.

## Dataset Description

The dataset contains historical transactions from a UK-based, registered, non-store online retailer that primarily sells gifts. Many of its customers are wholesalers.

The original dataset includes the following columns:

- `InvoiceNo`: Invoice number identifying a transaction. Values beginning with `C` indicate cancellations.
- `StockCode`: Product identifier.
- `Description`: Product description.
- `Quantity`: Quantity of products in a transaction.
- `InvoiceDate`: Date and time of the transaction.
- `UnitPrice`: Price per unit in British pounds.
- `CustomerID`: Customer identifier.
- `Country`: Customer's country.

## Data Period

1 December 2010 to 9 December 2011.

## Dataset Size

- **Original records:** 541,909 transactions.
- **Original columns:** 8.

The cleaned dataset may contain fewer records or different column values because of the data-cleaning process.

## Missing Values in the Project File

Although the UCI page labels the dataset as having no missing values, inspection of this project's local raw CSV found missing entries in two columns:

- `Description`: 1,454 missing values (0.27%).
- `CustomerID`: 135,080 missing values (24.93%).

These counts describe `data/online_retail.csv`, the file used in this project. The cleaning script fills missing descriptions with `Unknown` and retains rows with missing customer IDs, since they remain useful for analyses that do not require customer-level identification. The source page's summary and the local file's observed values differ; this documentation reports the values actually found in the project file.

## Attribution and License

- **Dataset creator:** Daqing Chen.
- **Original source:** UCI Machine Learning Repository.
- **License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
- **Dataset citation:** Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C5BW33](https://doi.org/10.24432/C5BW33)

Attribution is provided to acknowledge the original dataset creator and source.

## Usage

This dataset is used for an educational data analytics project involving data cleaning, exploratory data analysis (EDA), data visualization, and business insight development.

The analysis explores sales patterns, product performance, revenue trends, and other business metrics derived from the transaction data.
