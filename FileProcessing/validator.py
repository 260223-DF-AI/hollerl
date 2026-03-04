from datetime import datetime
import re
from exceptions import InvalidDataError, MissingFieldError

def validate_sales_record(record, line_number):
    """
    Validate a single sales record.
    
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number
    
    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError
    """

    try:
        match = re.fullmatch("STORE\\d{3}", record["store_id"])
    except KeyError as e:
        raise MissingFieldError(f"Missing required field store_id") from e
    except TypeError as e:
        raise InvalidDataError(f"Store ID cannot have a value of None") from e
    if not match:
        raise InvalidDataError(f"Invalid store format {record['store_id']}")

    try:
        datetime.strptime(record["date"], "%Y-%m-%d")
    except KeyError as e:
        raise MissingFieldError(f"Missing required field date") from e
    except ValueError as e:
        raise InvalidDataError(f"Invalid date format {record['date']}") from e
    except TypeError as e:
        raise InvalidDataError(f"Date cannot have a value of None") from e

    try:
        valid_quantity = int(record["quantity"])
    except KeyError as e:
        raise MissingFieldError(f"Missing required field quantity") from e
    except ValueError as e:
        raise InvalidDataError(f"Invalid quantity {record['quantity']}") from e
    except TypeError as e:
        raise InvalidDataError(f"Quantity cannot have a value of None") from e
    if valid_quantity <= 0:
        raise InvalidDataError(f"Quantity must be a positive, got {record['quantity']}")
    record['quantity'] = valid_quantity

    try:
        valid_price = float(record["price"])
    except KeyError as e:
        raise MissingFieldError(f"Missing required field price")
    except ValueError as e:
        raise InvalidDataError(f"Invalid price {record['price']}") from e
    except TypeError as e:
        raise InvalidDataError(f"Price cannot have a value of None") from e
    if valid_quantity <= 0:
        raise InvalidDataError(f"Price must be a positive, got {record['price']}")
    record["price"] = valid_price

    return record

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    all_records = ([], [])
    for index, line in enumerate(records):
        try:
            all_records[0].append(validate_sales_record(line, index))
        except Exception as e:
            all_records[1].append(f"    - Line {index + 1}: {str(e)}")
    return all_records