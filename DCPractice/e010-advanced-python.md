# Lab: Advanced Python - Decorators and Generators

## Overview

In this exercise, you will create a caching decorator and data processing generators to practice advanced Python patterns.

**Mode:** Implementation (Code Lab)
**Estimated Time:** 3-4 hours
**Prerequisites:** Content c071-c074 (Generators, Generator Expressions, Decorators, functools)

---

## Learning Objectives

By completing this exercise, you will be able to:

- Create custom decorators with and without arguments
- Use functools.wraps to preserve function metadata
- Build generator functions for memory-efficient processing
- Chain generators into processing pipelines
- Apply functools patterns (partial, lru_cache)

---

## The Scenario

You are building a data processing library for your team. The library needs:

1. Decorators for common cross-cutting concerns (logging, timing, caching, retry)
2. Generators for processing large files without loading them entirely into memory
3. A processing pipeline that chains multiple transformations

---

## Core Tasks

### Part 1: Custom Decorators (90 min)

Create `decorators.py` with the following:

#### Task 1.1: Timer Decorator (20 min)

```python
from functools import wraps
import time

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    pass
```

#### Task 1.2: Logger Decorator (20 min)

```python
def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    pass
```

#### Task 1.3: Retry Decorator with Arguments (30 min)

```python
def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    pass
```

#### Task 1.4: Cache Decorator (30 min)

```python
def cache(max_size=128):
    """
    Cache function results.
    Similar to lru_cache but with visible cache inspection.
    
    Usage:
        @cache(max_size=100)
        def expensive_computation(x):
            return x ** 2
        
        expensive_computation(5)  # Computes
        expensive_computation(5)  # Returns cached
        
        # Inspect cache
        expensive_computation.cache_info()
        expensive_computation.cache_clear()
    """
    pass
```

### Part 2: Generator Functions (60 min)

Create `generators.py` with the following:

#### Task 2.1: File Line Generator (20 min)

```python
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
    pass
```

#### Task 2.2: Batch Generator (20 min)

```python
def batch(iterable, size):
    """
    Yield items in batches of the specified size.
    
    Usage:
        list(batch([1,2,3,4,5,6,7], 3))
        # [[1,2,3], [4,5,6], [7]]
    """
    pass
```

#### Task 2.3: Filter Generator (20 min)

```python
def filter_by(iterable, predicate):
    """
    Yield items that match the predicate.
    
    Usage:
        evens = filter_by(range(10), lambda x: x % 2 == 0)
        list(evens)  # [0, 2, 4, 6, 8]
    """
    pass


def filter_errors(log_lines):
    """
    Yield only lines containing 'ERROR'.
    """
    pass


def filter_by_field(records, field, value):
    """
    Yield records where record[field] == value.
    
    Usage:
        active_users = filter_by_field(users, 'status', 'active')
    """
    pass
```

### Part 3: Generator Pipeline (45 min)

Create `pipeline.py`:

```python
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
    pass


# Example pipeline stages:

def parse_csv_line(lines):
    """Convert CSV lines to dictionaries."""
    pass


def validate_records(records):
    """Yield only valid records, skip invalid ones."""
    pass


def enrich_records(records):
    """Add calculated fields to each record."""
    pass


def deduplicate(records, key_field):
    """Yield unique records based on a key field."""
    pass
```

### Part 4: Practical Application (45 min)

Create `log_analyzer.py` that uses your decorators and generators:

```python
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
    pass


@cache(max_size=1000)
def parse_log_line(line):
    """
    Parse a single log line into structured data.
    Cached because the same line format appears often.
    """
    pass


def count_by_level(log_path):
    """
    Count log entries by level (INFO, WARNING, ERROR).
    Use generators to process without loading entire file.
    """
    pass


def get_error_summary(log_path, top_n=10):
    """
    Get top N most common error messages.
    """
    pass


def process_logs_in_batches(log_path, batch_size=1000):
    """
    Process logs in batches for database insertion.
    Yields batches of parsed log entries.
    """
    pass
```

### Part 5: Tests (30 min)

Create `test_decorators.py` and `test_generators.py`:

```python
import pytest
from decorators import timer, retry, cache

def test_timer_returns_result():
    """Timer decorator should not affect return value."""
    pass

def test_retry_succeeds_eventually():
    """Retry should succeed if function works within attempts."""
    pass

def test_cache_returns_cached_value():
    """Cache should return same value without recomputing."""
    pass

def test_cache_info_tracks_hits():
    """Cache info should track hits and misses."""
    pass
```

```python
import pytest
from generators import read_lines, batch, filter_by

def test_batch_correct_sizes():
    """Batch should yield correct batch sizes."""
    result = list(batch(range(7), 3))
    assert len(result) == 3
    assert len(result[0]) == 3
    assert len(result[2]) == 1

def test_filter_by_predicate():
    """Filter should only yield matching items."""
    pass

def test_read_lines_skips_empty():
    """Read lines should skip empty lines."""
    pass
```

---

## Sample Log File

Create `samples/app.log`:

```
2024-01-15 10:00:00 INFO Application started
2024-01-15 10:00:01 INFO Loading configuration
2024-01-15 10:00:02 WARNING Config key 'timeout' not found, using default
2024-01-15 10:00:05 INFO Processing batch 1
2024-01-15 10:00:06 ERROR Database connection failed: timeout
2024-01-15 10:00:07 INFO Retrying connection
2024-01-15 10:00:08 ERROR Database connection failed: refused
2024-01-15 10:00:10 INFO Connection established
2024-01-15 10:00:15 INFO Processing batch 2
2024-01-15 10:00:20 WARNING Slow query detected: 5.2s
2024-01-15 10:00:25 INFO Processing complete
2024-01-15 10:00:26 INFO Application shutdown
```

---

## Expected Output

```
=== Log Analysis ===

analyze_logs took 0.0234 seconds

Log Level Counts:
- INFO: 8
- WARNING: 2
- ERROR: 2

Top Error Messages:
1. "Database connection failed: timeout" (1)
2. "Database connection failed: refused" (1)

Cache Statistics:
- Hits: 45
- Misses: 12
- Hit Rate: 78.9%
```

---

## Definition of Done

- [ ] All 4 decorators work correctly
- [ ] Decorators preserve function metadata (@wraps)
- [ ] Generator functions yield values lazily
- [ ] Pipeline chains generators properly
- [ ] Log analyzer processes files efficiently
- [ ] At least 8 tests pass
- [ ] No full file loads into memory for large files

---

## Stretch Goals (Optional)

1. Add an `@async_retry` decorator for async functions
2. Implement a `@rate_limit` decorator
3. Create a `@validate_args` decorator using type hints
4. Build a generator that processes multiple files in parallel

---

## Submission

1. Ensure all modules are complete
2. Run the log analyzer on the sample file
3. Run all tests
4. Document the memory efficiency of your generators
5. Be prepared to explain decorator execution order
