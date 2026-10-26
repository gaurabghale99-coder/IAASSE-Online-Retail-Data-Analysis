import pandas as pd

df = pd.read_csv(
    "data/online_retail.csv"
)

print("Shape:" , df.shape)


print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nFirst 5 rows:")
print(df.head())


# Check rows with missing Description
print("\nRows with missing Description:")
print(df[df["Description"].isnull()].head())


# Check rows with missing CustomerID
print("\nRows with missing CustomerID:")
print(df[df["CustomerID"].isnull()].head())


# Check percentage of missing values
print("\nMissing value percentage:")
print(((df.isnull().sum() / len(df)) * 100 ).round(2))



# Handle missing Description
df["Description"] = df["Description"].fillna("Unknown")

# Keep missing CustomerID values
# CustomerID will be excluded only when customer-specific analysis is performed.

print("\nMissing values after handling Description:")
print(df.isnull().sum())


# Remove duplicate rows
df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)



# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nData types after conversion:")
print(df.dtypes)



# Check numeric columns

print("\nQuantity Statistics:")
print(df["Quantity"].describe())

print("\nUnitPrice Statistics:")
print(df["UnitPrice"].describe())


# Check negative quantities

print("\nRow with negative Quantity:")
print(df[df["Quantity"] < 0].head(10))


print("\nRow with Quantity greater than 10000:")
print(df[df["Quantity"] > 10000])



print("\nRow with negative UnitPrice:")
print(df[df["UnitPrice"] < 0].head(10))


print("\nRow with UnitPrice greater than 1000:")
print(df[df["UnitPrice"] > 1000])



# Remove rows with negative unitprice

df = df[df["UnitPrice"] >= 0]

print("\nShape after removing negative unitprice rows:")
print(df.shape)


# Check extreme quantities

quantity_outliers = df[df["Quantity"].abs() > 10000]

print("\nExtreme quantity values:")
print(quantity_outliers[["InvoiceNo" , "StockCode", "Quantity"]])




# Final validation

print("\nFinal Shape:")
print(df.shape)

print("\nFinal Missing values:")
print(df.isnull().sum())

print("\nFinal Duplicate count:")
print(df.duplicated().sum())

print("\nFinal Data types:")
print(df.dtypes)


# Save cleaned dataset

df.to_csv(
    "data/online_retail_cleaned.csv",
    index= False
)

print("\nCleaned Dataset Saved successfully....")