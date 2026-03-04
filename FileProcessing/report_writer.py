from datetime import datetime
from file_reader import read_csv_file

def write_summary_report(filepath, valid_records, errors, store_sales, product_sales):
    """
    Write a formatted summary report.
    
    Report should include:
    - Processing timestamp
    - Total records processed
    - Number of valid records
    - Number of errors (with details)
    - Sales by store
    - Top 5 products
    """

    print(f"""
    === Sales Processing Report ===
    Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    Processing Statistics:
    - Total records: {len(valid_records) + len(errors)}
    - Valid records: {len(valid_records)}
    - Error records: {len(errors)}

    Errors:""")
    for err in errors:
        print(err)
    print("""

    Sales by Store:
    """)
    for store, sales in store_sales.items():
        print(f"    - {store}: ${sales}")
    print("""
    
    Top Products:
    """)
    sorted_product_sales = dict(sorted(product_sales.items(), key=lambda item: item[1], reverse = True))
    first_five = dict(list(sorted_product_sales.items())[:5])
    for product, sales in first_five.items():
        print(f"    - {product}: {sales} units")

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    with open(filepath, "w") as f:
        f.write(records)

def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    with open(filepath, "w") as f:
        for err in errors:
            f.write(err + "\n")