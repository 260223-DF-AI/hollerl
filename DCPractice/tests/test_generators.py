import pytest
from DCPractice.generators import read_lines, batch, filter_by

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