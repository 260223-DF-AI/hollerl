from functools import wraps
import time

from pygments.lexers import func


def timer(func):
    """
    Measure and print function execution time.

    Usage:
        @timer
        def slow_function():
            time.sleep(1)

    Output: "slow_function took 1.0023 seconds"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


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

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Format arguments for printing
        args_str = ", ".join(str(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        all_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"Calling {func.__name__}({all_args})")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result

    return wrapper


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
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except exceptions:
                time.sleep(delay)

    return wrapper


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
    def decorator(func):
        cache_store = {}
        cache_order = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            # Return cached result
            if key in cache_store:
                return cache_store[key]

            # Compute result
            result = func(*args, **kwargs)

            # Maintain cache size
            if len(cache_store) >= max_size:
                oldest = cache_order.pop(0)
                del cache_store[oldest]

            cache_store[key] = result
            cache_order.append(key)

            return result

        # Cache inspection
        def cache_info():
            return {
                "size": len(cache_store),
                "max_size": max_size
            }

        # Cache clearing
        def cache_clear():
            cache_store.clear()
            cache_order.clear()

        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    return decorator


