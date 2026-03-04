def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    for index, line in enumerate(records):
        records[index]["total"] = round(records[index]["quantity"] * records[index]["price"], 2)
    return records

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    store_sales = {}
    for line in records:
        if line["store_id"] not in store_sales:
            store_sales[line["store_id"]] = line["total"]
        else:
            store_sales[line["store_id"]] += line["total"]
    return store_sales

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    product_sales = {}
    for line in records:
        if line["product"] not in product_sales:
            product_sales[line["product"]] = line["quantity"]
        else:
            product_sales[line["product"]] += line["quantity"]
    return product_sales