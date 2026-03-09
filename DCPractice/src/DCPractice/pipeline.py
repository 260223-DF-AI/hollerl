import csv


def create_pipeline(*stages):
    """
    Create a processing pipeline from multiple generator functions.

    Usage:
        pipeline = create_pipeline(
            read_lines,
            parse_json,
            filter_valid,
            transform
        )

        for result in pipeline('input.json'):
            save(result)
    """
    def run_pipeline(initial_input):
        output = initial_input
        for stage in stages:
            output = stage(output)
        return output

    return run_pipeline

    def run_pipeline(initial_input):
        output = initial_input
        for stage in stages:
            output = stage(output)  # pass output to next stage
        return output

    return run_pipeline


def parse_csv_line(lines):
    """Convert CSV lines to dictionaries."""
    reader = csv.DictReader(lines)
    for row in reader:
        yield dict(row)


def validate_records(records):
    """Yield only valid records, skip invalid ones."""
    for record in records:
        # Skip if not a dictionary
        if not isinstance(record, dict):
            continue

        # Skip if any value is None or empty
        if any(v is None or v == "" for v in record.values()):
            continue

        # Passed all checks, yield the valid record
        yield record


def enrich_records(records):
    """Add calculated fields to each record."""
    for record in records:
        enriched = dict(record)  # avoid mutating original

        # Boolean column indicating missing values
        enriched["has_null"] = any(v is None for v in record.values())

        yield enriched


def deduplicate(records, key_field):
    """Yield unique records based on a key field."""
    seen = {}

    for record in records:
        key = record.get(key_field)

        if key is None:
            continue

        if key in seen:
            continue

        seen.add(key)
        yield record