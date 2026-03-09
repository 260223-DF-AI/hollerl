from decorators import timer, logger, cache
from generators import read_lines, batch, filter_errors
from pipeline import create_pipeline


@timer
@logger
def analyze_logs(log_path):
    """
    Analyze a log file and return statistics.

    Uses generators for memory-efficient processing.
    Uses decorators for timing and logging.
    """
    stats = {
        "total_lines": 0,
        "error_count": 0
    }

    pipeline = create_pipeline(
        read_lines,
        filter_errors
    )

    for line in pipeline(log_path):
        stats["error_count"] += 1

    # count total lines separately
    for _ in read_lines(log_path):
        stats["total_lines"] += 1

    return stats


@cache(max_size=1000)
def parse_log_line(line):
    """
    Parse a single log line into structured data.
    Cached because the same line format appears often.
    """
    parts = line.split(" ", 2)

    if len(parts) < 3:
        return {
            "timestamp": None,
            "level": None,
            "message": line
        }

    timestamp, level, message = parts

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }


def count_by_level(log_path):
    """
    Count log entries by level (INFO, WARNING, ERROR).
    Use generators to process without loading entire file.
    """
    counts = Counter()

    for line in read_lines(log_path):
        record = parse_log_line(line)
        level = record["level"]

        if level:
            counts[level] += 1

    return dict(counts)


def get_error_summary(log_path, top_n=10):
    """
    Get top N most common error messages.
    """
    counter = Counter()

    pipeline = create_pipeline(
        read_lines,
        filter_errors
    )

    for line in pipeline(log_path):
        record = parse_log_line(line)
        counter[record["message"]] += 1

    return counter.most_common(top_n)


def process_logs_in_batches(log_path, batch_size=1000):
    """
    Process logs in batches for database insertion.
    Yields batches of parsed log entries.
    """
    def parsed_lines(lines):
        for line in lines:
            yield parse_log_line(line)

    pipeline = create_pipeline(
        read_lines,
        parsed_lines
    )

    for b in batch(pipeline(log_path), batch_size):
        yield b