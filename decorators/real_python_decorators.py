import functools


def simple_decorator(func):
    def wrapper():
        print("before func")
        func()
        print('after func')
    return wrapper


def do_twice_decorator(func):
    def wrapper(*args):
        print("before func")
        func(*args)
        return func(*args)
        print('after func')
    return wrapper


def say_ello_bro():
    print('ello_bro')


@simple_decorator
def say_ello_decorator():
    print('ello_decorator')


@do_twice_decorator
def say_with_arg(arg):
    print('simple print say with arg')
    return f'Say with arg Return: {arg}'


say_ello_bro = simple_decorator(say_ello_bro)

# say_ello_bro()
# print('---------------------------------------')
# say_ello_decorator()
# print('---------------------------------------')
# say_with_arg('ARG')
# print('---------------------------------------')
# print(say_with_arg("Do you see me ?"))
# print('---------------------------------------')

# Functools


def functools_decorator(func):
    @functools.wraps(func)
    def wrapper_functools_decorator(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_functools_decorator


@functools_decorator
def say_ello_to_the_functools(greeting):
    print(greeting)
    return 1


# greet = say_ello_to_the_functools('Ello functools')
# print(greet)

# Decorators with Arguments




