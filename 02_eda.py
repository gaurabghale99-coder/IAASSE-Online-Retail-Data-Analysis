import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from pathlib import Path


output_dir = Path("outputs/visualizations")
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/online_retail_cleaned.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


# revenue column
df["Revenue"] =  df["Quantity"] * df["UnitPrice"]


print(df.head())

print(df.describe())

print(df.info())


# Step 2: EDA visualizations


fig, axes = plt.subplots(1, 2 , figsize =(12, 5))

sns.histplot(df["Quantity"] , bins=50 , ax=axes[0])
axes[0].set_title("Quantity Distribution")
axes[0].set_xlim(
    df["Quantity"].quantile(0.01),
    df["Quantity"].quantile(0.99)
)

sns.histplot(df["UnitPrice"] , bins=50 , ax=axes[1])
axes[1].set_title("Unit Price Distribution")
axes[1].set_xlim(
    df["UnitPrice"].quantile(0.01),
    df["UnitPrice"].quantile(0.99)
)


plt.tight_layout()
plt.savefig(output_dir / "quantity_unitprice_distribution.png",
            dpi=300, bbox_inches="tight")
plt.show()



# correlation heatmap

numeric_cols = [
    "Quantity",
    "UnitPrice",
    "Revenue",
]

correlation  = df[numeric_cols].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)


plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig(output_dir / "correlation_heatmap.png",
            dpi=300, bbox_inches="tight")
plt.show()



# monthly revenue trend


df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = df.groupby("Month")["Revenue"].sum()

monthly_revenue.index = monthly_revenue.index.astype(str)

monthly_revenue.plot(
    figsize=(12,5),
    marker = "o"
)

plt.title("Monthly Net Recorded Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Net Recorded Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(output_dir / "monthly_revenue_trend.png",
            dpi=300, bbox_inches="tight")

plt.show()


# top 10 products by qunatity sold

top_products = (
    df[
        (df["Quantity"] > 0) &
        (df["Description"] != "Unknown")
    ]
    .groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.plot(
    kind="barh", 
    figsize=(10,6)
)

plt.title("Top 10 prodcuts by Quantity")
plt.xlabel("Total Quantity")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(output_dir / "top_10_products.png",
            dpi=300, bbox_inches="tight")
plt.show()



# detect unusual values

print("Negative Quantities:")
print(df[df["Quantity"] < 0].head())

print("Zero or Negative Unit Price:")
print(df[df["UnitPrice"] <= 0].head())


print("Highest Quantities:")
print(
    df.nlargest(10, "Quantity")[
        ["InvoiceNo", "Description", "Quantity", "UnitPrice"]
    ]
)

print("Highest Unit Prices:")
print(
    df.nlargest(10, "UnitPrice")[
        ["InvoiceNo", "Description", "Quantity", "UnitPrice"]
    ]
)    



# Investigate unusual values properly


# investigate negative quantities

negative_qty = df[df["Quantity"] < 0] 

print("Total records with negative quantity:", len(negative_qty))

print("Invoice numbers of negative quantities:")
print(negative_qty["InvoiceNo"].value_counts().head(10))

print("\nSample negative quantity records:")
print(
    negative_qty[
        ["InvoiceNo", "Description", "Quantity", "UnitPrice", "Revenue"]
    ].head(10)
)



# investigate zero or negative unit price 

invalid_prices = df[df["UnitPrice"] <= 0]

print("\nRecords with zero or negative unit price:")
print(len(invalid_prices))

print(
    invalid_prices[
        ["InvoiceNo", "Description", "Quantity", "UnitPrice"]
    ].head(10)
)




# Detect outliers using the IQR method

for col in ["Quantity", "UnitPrice"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[col] < lower_limit) |
        (df[col] > upper_limit) 
    ]

    print(f"\nOutliers in {col}")
    print("Lower Limit:" , lower_limit)
    print("Upper Limit:" , upper_limit)
    print("Number of outliers:", len(outliers))




# one more useful trend analysis
# monthly order volume


df["Month"] = df["InvoiceDate"].dt.to_period("M")


monthly_orders = (
    df.groupby("Month")["InvoiceNo"]
    .nunique()
)


monthly_orders.index = monthly_orders.index.astype(str)


monthly_orders.plot(
    figsize=(12, 5),
    marker= "o"
)

plt.title("Monthly Order volume Trend")
plt.xlabel("Month")
plt.ylabel("Number of Unique Invoices")
plt.xticks(rotation= 45)
plt.tight_layout()

plt.savefig(output_dir / "monthly_order_volume.png",
            dpi=300, bbox_inches="tight")

plt.show()