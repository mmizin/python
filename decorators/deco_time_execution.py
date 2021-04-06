import functools
import time


def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {execution_time:.4f} secs')
        return result
    return wrapper


@timer_decorator
def some_function(start, end):
    for _ in range(start, end):
        pass

    return 1


some_function(1, 1000000)
