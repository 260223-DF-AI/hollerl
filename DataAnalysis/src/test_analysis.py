import pytest
import pandas as pd
from analysis import *

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        'order_id': [1, 2, 3],
        'customer_id': ['C001', 'C002', 'C001'],
        'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-02']),
        'product_name': ['Widget', 'Gadget', 'Widget'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'quantity': [2, 1, 3],
        'unit_price': [10.00, 25.00, 10.00],
        'region': ['North', 'South', 'North']
    })

def test_clean_data_removes_duplicates(sample_data):
    """Test that clean_data removes duplicate rows."""
    dupe_data = pd.concat([sample_data, sample_data.loc[[1]]], ignore_index=True)
    cleaned_data = clean_data(dupe_data)
    pd.testing.assert_frame_equal(sample_data, cleaned_data.drop(columns=["total_sales"]))

def test_clean_data_by_total_sales_calculations(sample_data):
    sample_data["total_sales"] = sample_data["quantity"] * sample_data["unit_price"]
    cleaned_data = clean_data(sample_data)
    pd.testing.assert_frame_equal(cleaned_data, sample_data)


def test_sales_by_category_calculation(sample_data):
    category_data = sales_by_category(clean_data(sample_data))
    assert category_data["total_sales"].mean() == clean_data(sample_data)["total_sales"].sum()


def test_sales_by_region_calculation(sample_data):
    region_data = sales_by_region(clean_data(sample_data))
    assert region_data["total_sales"].sum() == clean_data(sample_data)["total_sales"].sum()


def test_top_products_returns_correct_count(sample_data):
    assert len(top_products(clean_data(sample_data))) == 2


def test_top_products_returns_correct_quantity(sample_data):
    assert top_products(clean_data(sample_data))["units_sold"].sum() == clean_data(sample_data)["quantity"].sum()


def test_daily_sales(sample_data):
    assert (daily_sales_trend(clean_data(sample_data))["total_sales"].sum() ==
            clean_data(sample_data)["total_sales"].sum())

def test_customer_analysis(sample_data):
    assert (customer_analysis(clean_data(sample_data))["total_spent"].sum() ==
            clean_data(sample_data)["total_sales"].sum())