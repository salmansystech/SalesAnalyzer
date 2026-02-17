import pandas as pd

# Load the CSV
df = pd.read_csv("sales.csv")

# Check the first 5 rows
print("First 5 rows of your data:")
print(df.head())

# Make sure your CSV has 'Region' and 'Sales' columns!
if 'Region' not in df.columns or 'Sales' not in df.columns:
    print("Your CSV must have 'Region' and 'Sales' columns!")
else:
    # Summary statistics of sales
    print("\nSummary statistics of Sales:")
    print(df["Sales"].describe())

    # Total sales by region
    total_sales_by_region = df.groupby("Region")["Sales"].sum()
    print("\nTotal Sales by Region:")
    print(total_sales_by_region)

    # Region with highest sales
    top_region = total_sales_by_region.idxmax()
    top_sales = total_sales_by_region.max()
    print(f"\nRegion with highest sales: {top_region} (${top_sales:.2f})")
