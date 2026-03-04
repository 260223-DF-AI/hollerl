import file_reader
import validator
import transformer
import report_writer
import sys

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
    records = file_reader.read_csv_file(input_path)
    records_tuple = validator.validate_all_records(records)
    records = records_tuple[0]
    errors = records_tuple[1]
    records = transformer.calculate_totals(records)
    store_sales = transformer.aggregate_by_store(records)
    product_sales = transformer.aggregate_by_product(records)
    report_writer.write_summary_report(input_path, records, errors, store_sales, product_sales)

    header = ",".join(records[0].keys())
    rows = []
    for r in records:
        rows.append(",".join(str(v) for v in r.values()))

    csv_string = "\n".join([header] + rows)

    report_writer.write_clean_csv(output_dir + "/cleaned_sales.csv", csv_string)
    report_writer.write_error_log(output_dir + "/errors.log", errors)


#process_sales_file("sample_sales.csv", ".")


if __name__ == "__main__":
    # Process from command line
    input_path = sys.argv[1]
    output_dir = sys.argv[2]
    process_sales_file(input_path, output_dir)
