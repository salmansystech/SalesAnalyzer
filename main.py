import pandas as pd
import sys
from pathlib import Path

def load_sales_data(filepath):
    """Load sales data from CSV file."""
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded {len(df)} records from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        sys.exit(1)

def generate_statistics(df):
    """Generate summary statistics from sales data."""
    print("\n=== Sales Statistics ===")
    print(f"Total Sales: ${df['Sales'].sum():,.2f}")
    print(f"Total Profit: ${df['Profit'].sum():,.2f}")
    print(f"Average Discount: {df['Discount'].mean():.2%}")
    
    print("\n=== Regional Summary ===")
    regional = df.groupby('Region')[['Sales', 'Profit']].sum()
    print(regional)
    
    return regional

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <sales_data.csv>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    df = load_sales_data(filepath)
    generate_statistics(df)

if __name__ == "__main__":
    main()
