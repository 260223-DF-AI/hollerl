import pandas as pd
import datetime

def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    return pd.read_csv(filepath)


def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    print(df.info())

def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_sales' = quantity * unit_price
    """
    df = df.drop_duplicates(ignore_index=True)
    # Dropped missing values
    df = df.dropna()
    df.columns = df.columns.str.strip().str.lower()
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["total_sales"] = df["quantity"] * df["unit_price"]
    return df

def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    df["day_of_week"] = pd.to_datetime(df["order_date"]).dt.weekday()
    df["month"] = pd.to_datetime(df["order_date"]).dt.month
    df["quarter"] = pd.to_datetime(df["order_date"]).dt.quarter
    df["is_weekend"] = pd.to_datetime(df["order_date"]).dt.weekday() > 4

def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    df_category = df.groupby("category").agg(
        total_sales=("total_sales", "sum"),
        quantity=("quantity", "sum"),
        avg_order_value=("total_sales", "mean")
        ).reset_index()

    df_category = df_category.sort_values("total_sales", ascending=False)

    return df_category

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    df_region = df.groupby("region", as_index=False).agg(
        total_sales= ("total_sales", "sum"))
    total = df_region["total_sales"].sum()
    df_region["percentage_of_total"] = round(df_region["total_sales"] / total * 100)

    return df_region

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    df_top_products = df.groupby("product_name", as_index=False).agg(
        category = ("category", "first"),
        total_sales = ("total_sales", "sum"),
        units_sold = ("quantity", "sum"))

    df_top_products = df_top_products.sort_values("total_sales", ascending=False)

    return df_top_products.head(n)

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    df_daily_sales = df.groupby("order_date", as_index=False).agg(
        total_sales = ("total_sales", "sum"),
        order_count = ("quantity", "sum"))

    df_daily_sales = df_daily_sales.sort_values("order_date")
    
    return df_daily_sales

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    df_customers = df.groupby("customer_id", as_index=False).agg(
        total_spent = ("total_sales", "sum"),
        order_count = ("order_id", "count"),
        avg_order_value = ("total_sales", "mean"),
        favorite_category = ("category", lambda x: x.mode()[0]))
    
    return df_customers

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    df_days = df.groupby("is_weekend", as_index=False).agg(
        total_sales = ("total_sales", "sum"))
    total = df_days["total_sales"].sum()
    df_days["percentage_of_total"] = df_days["total_sales"] / total * 100

    dict = {"weekend_total_sales" : df_days[df_days["is_weekend"] == True]["total_sales"].values[0],
            "weekday_total_sales" : df_days[df_days["is_weekend"] == False]["total_sales"].values[0],
            "weekend_percentage" : df_days[df_days["is_weekend"] == True]["percentage_of_total"].values[0],
            "weekday_percentage" : df_days[df_days["is_weekend"] == False]["percentage_of_total"].values[0]}

    return dict