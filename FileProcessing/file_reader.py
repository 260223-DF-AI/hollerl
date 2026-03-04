from exceptions import FileProcessingError
import logging

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
    try:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            with open(filepath, "r", encoding="latin-1") as f:
                lines = f.readlines()

    except FileNotFoundError as e:
        logging.error(f"File not found: {filepath}")
        raise FileProcessingError(f"File not found: {filepath}") from e

    except UnicodeDecodeError as e:
        logging.error(f"Unable to decode file: {filepath}")
        raise FileProcessingError(f"Unable to decode file: {filepath}") from e

    if not lines:
        return []

    headers = lines[0].strip().split(",")

    data = []

    for line in lines[1:]:
        values = line.strip().split(",")

        row_dict = dict(zip(headers, values))
        data.append(row_dict)

    return data