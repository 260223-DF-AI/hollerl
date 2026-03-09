def read_lines(filepath, encoding='utf-8'):
    """
    Yield lines from a file one at a time.
    - Strip whitespace from each line
    - Skip empty lines
    - Handle encoding errors gracefully

    Usage:
        for line in read_lines('large_file.txt'):
            process(line)
    """
    try:
        with open(filepath, 'r', encoding=encoding, errors='replace') as f:
            for line in f:
                line = line.strip()

                if not line:  # skip empty lines
                    continue

                yield line

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except OSError as e:
        print(f"Error reading file: {e}")


def batch(iterable, size):
    """
    Yield items in batches of the specified size.

    Usage:
        list(batch([1,2,3,4,5,6,7], 3))
        # [[1,2,3], [4,5,6], [7]]
    """
    current_batch = []

    for item in iterable:
        current_batch.append(item)

        if len(current_batch) == size:
            yield current_batch
            current_batch = []

    if current_batch:
        yield current_batch


def filter_by(iterable, predicate):
    """
    Yield items that match the predicate.

    Usage:
        evens = filter_by(range(10), lambda x: x % 2 == 0)
        list(evens)  # [0, 2, 4, 6, 8]
    """
    for item in iterable:
        if predicate(item):
            yield item


def filter_errors(log_lines):
    """
    Yield only lines containing 'ERROR'.
    """
    for line in log_lines:
        if 'ERROR' in line:
            yield line


def filter_by_field(records, field, value):
    """
    Yield records where record[field] == value.

    Usage:
        active_users = filter_by_field(users, 'status', 'active')
    """
    for record in records:
        if record[field] == value:
            yield record