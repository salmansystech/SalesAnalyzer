import pandas as pd
from typing import Tuple

def calculate_regional_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate sales metrics by region."""
    return df.groupby('Region').agg({
        'Sales': ['sum', 'mean', 'count'],
        'Profit': ['sum', 'mean'],
        'Discount': 'mean'
    }).round(2)

def identify_trends(df: pd.DataFrame) -> dict:
    """Identify sales trends over time."""
    df['Date'] = pd.to_datetime(df['Date'])
    monthly = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
    
    return {
        'total_sales': df['Sales'].sum(),
        'total_profit': df['Profit'].sum(),
        'avg_discount': df['Discount'].mean(),
        'monthly_trend': monthly.to_dict()
    }

def find_top_performers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Find top performing regions."""
    return df.groupby('Region')['Profit'].sum().nlargest(n)
