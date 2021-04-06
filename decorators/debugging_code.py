import functools
import math

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f'{k}={v!r}' for k,v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__!r}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper


@debug
def some_func(name, params):
    return True


some_func('debug', {'key': 'wrapper'})

print('------------------------------------')

math.factorial = debug(math.factorial)


def approximate_e(terms=3):
    return sum(1 / math.factorial(n) for n in range(terms))


approximate_e()