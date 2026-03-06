import matplotlib.pyplot as plt
import numpy as np

import analysis

def create_category_bar_chart(category_data, output_path):
    """
    Create a horizontal bar chart of sales by category.
    - Include value labels on bars
    - Use a professional color scheme
    - Save to output_path
    """

    fig, ax = plt.subplots()
    bars = ax.barh(category_data["category"], category_data["total_sales"], color=["blue"])

    ax.bar_label(bars, labels = [f"${width:,.0f}" for width in category_data["total_sales"]])
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Category")
    ax.set_title("Total Sales by Category")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close(fig)

def create_regional_pie_chart(region_data, output_path):
    """
    Create a pie chart showing sales distribution by region.
    - Include percentages
    - Use distinct colors for each region
    - Save to output_path
    """
    fig, ax = plt.subplots()
    ax.pie(region_data["total_sales"],
           labels=[f"{per:,.0f}%" for per in region_data["percentage_of_total"]],
           colors=["blue", "red"])
    ax.set_title("Sales Distribution by Region")
    ax.legend(region_data["region"])

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close(fig)

def create_sales_trend_line(daily_data, output_path):
    """
    Create a line chart showing daily sales trend.
    - Include moving average (7-day)
    - Mark weekends differently
    - Add proper axis labels and title
    - Save to output_path
    """
    fig, ax = plt.subplots()
    ax.plot(daily_data["order_date"], daily_data["total_sales"], label="Daily Sales", color="blue")

    daily_data["ma_7"] = daily_data.rolling("7D", on="order_date")["total_sales"].mean()

    ax.plot(daily_data["order_date"], daily_data["ma_7"], label="7-Day Moving Avg", color="green")

    ax.set_xlabel("Date")
    ax.set_ylabel("Daily Sales")
    ax.set_title("Total Sales Trends")
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close(fig)

def create_dashboard(df, output_dir):
    """
    Create a multi-panel dashboard with 4 subplots:
    1. Sales by category (bar)
    2. Sales by region (pie)
    3. Daily trend (line)
    4. Top 10 products (horizontal bar)
    
    Save as a single figure.
    """
    category_data = analysis.sales_by_category(df)
    region_data = analysis.sales_by_region(df)
    daily_data = analysis.daily_sales_trend(df)
    daily_data["ma_7"] = daily_data.rolling("7D", on="order_date")["total_sales"].mean()
    top_data = analysis.top_products(df)

    # --- Create multi-panel figure ---
    fig, axes = plt.subplots(2, 2, figsize=(10,10))

    # --- 1. Category Bar Chart ---
    ax = axes[0,0]
    bars = ax.barh(category_data["category"], category_data["total_sales"], color=["blue"])

    ax.bar_label(bars, labels = [f"${width:,.0f}" for width in category_data["total_sales"]])
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Category")
    ax.set_title("Total Sales by Category")

    # --- 2. Region Pie Chart ---
    ax = axes[0,1]
    ax.pie(region_data["total_sales"],
           labels=[f"{per:,.0f}%" for per in region_data["percentage_of_total"]],
           colors=["blue", "red"])
    ax.set_title("Sales Distribution by Region")
    ax.legend(region_data["region"])

    # --- 3. Daily Trend Line ---
    ax = axes[1,0]
    ax.plot(daily_data["order_date"], daily_data["total_sales"], label="Daily Sales", color="blue")
    ax.plot(daily_data["order_date"], daily_data["ma_7"], label="7-Day Moving Avg", color="green")

    ax.set_xlabel("Date")
    ax.set_ylabel("Daily Sales")
    ax.set_title("Total Sales Trends")

    ax = axes[1,1]
    bars = ax.barh(top_data["product_name"], top_data["total_sales"], color=["blue"])

    ax.bar_label(bars, labels = [f"${width:,.0f}" for width in category_data["total_sales"]])
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Product")
    ax.set_title("Top Product Sales")

    plt.tight_layout()
    plt.savefig(output_dir)
    plt.close(fig)