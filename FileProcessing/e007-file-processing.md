# Lab: File Processing Pipeline

## Overview

In this exercise, you will build a file processor that reads, transforms, and writes data while implementing proper error handling and context management.

**Mode:** Implementation (Code Lab)
**Estimated Time:** 3-4 hours
**Prerequisites:** Content c054-c061 (Errors, Exception Handling, File Handling)

---

## Learning Objectives

By completing this exercise, you will be able to:

- Read and parse data from various file formats
- Handle file-related exceptions gracefully
- Use context managers for resource management
- Write processed data to output files
- Create custom exceptions for domain-specific errors

---

## The Scenario

Your company receives daily sales reports in CSV format from multiple stores. The files often contain errors (missing values, invalid data, encoding issues). You need to build a robust file processor that can:

1. Read the raw CSV files
2. Validate and clean the data
3. Generate summary reports
4. Handle errors without crashing

---

## Starter Files

Navigate to `starter_code/` and you will find:

- `sample_sales.csv` - A sample input file with some errors
- `processor.py` - Skeleton code to complete

---

## Core Tasks

### Task 1: Create Custom Exceptions (30 min)

Create a file `exceptions.py` with the following custom exceptions:

```python
class FileProcessingError(Exception):
    """Base exception for file processing errors."""
    pass

class InvalidDataError(FileProcessingError):
    """Raised when data validation fails."""
    pass

class MissingFieldError(FileProcessingError):
    """Raised when a required field is missing."""
    pass
```

### Task 2: Implement File Reader (45 min)

Create a `file_reader.py` module with:

```python
def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    pass
```

Requirements:

- Use context managers (`with` statement)
- Log errors before re-raising
- Return empty list for empty files (not an error)

### Task 3: Implement Data Validator (45 min)

Create a `validator.py` module with:

```python
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
    pass

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    pass
```

### Task 4: Implement Data Transformer (30 min)

Create a `transformer.py` module with:

```python
def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    pass

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    pass

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    pass
```

### Task 5: Implement Report Writer (45 min)

Create a `report_writer.py` module with:

```python
def write_summary_report(filepath, valid_records, errors, aggregations):
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
    pass

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    pass

def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    pass
```

### Task 6: Build the Pipeline (45 min)

Create `processor.py` that ties everything together:

```python
def process_sales_file(input_path, output_dir):
    """
    Main processing pipeline.
    
    1. Read the input file
    2. Validate all records
    3. Transform valid records
    4. Generate reports
    5. Handle any errors gracefully
    
    Returns: ProcessingResult with statistics
    """
    pass

if __name__ == "__main__":
    # Process from command line
    pass
```

---

## Sample Input (`sample_sales.csv`)

```csv
date,store_id,product,quantity,price
2024-01-15,STORE001,Widget A,10,29.99
2024-01-15,STORE002,Gadget B,5,49.99
invalid-date,STORE001,Widget A,3,29.99
2024-01-16,STORE003,Widget C,-2,19.99
2024-01-16,,Product X,8,15.00
2024-01-16,STORE002,Gadget B,abc,49.99
2024-01-17,STORE001,Widget A,12,29.99
```

---

## Expected Output

**summary_report.txt:**

```
=== Sales Processing Report ===
Generated: 2024-01-18 10:30:00

Processing Statistics:
- Total records: 7
- Valid records: 3
- Error records: 4

Errors:
- Line 3: Invalid date format 'invalid-date'
- Line 4: Quantity must be positive, got -2
- Line 5: Missing required field 'store_id'
- Line 6: Invalid quantity 'abc'

Sales by Store:
- STORE001: $659.78
- STORE002: $249.95

Top Products:
1. Widget A: 22 units
2. Gadget B: 5 units
```

---

## Definition of Done

- [ ] All custom exceptions are defined
- [ ] File reader handles encoding and missing files
- [ ] Validator catches all error types without crashing
- [ ] Transformer correctly calculates totals and aggregations
- [ ] Reports are generated in proper format
- [ ] Pipeline processes the sample file successfully
- [ ] Errors are logged, not swallowed

---

## Stretch Goals (Optional)

1. Add support for JSON input files
2. Implement a retry mechanism for transient file errors
3. Add a `--verbose` flag for detailed logging
4. Create a context manager for the entire pipeline that cleans up on failure

---

## Submission

1. Ensure all modules are complete and tested
2. Process the sample file and verify outputs
3. Be prepared to demonstrate error handling by introducing bad data
