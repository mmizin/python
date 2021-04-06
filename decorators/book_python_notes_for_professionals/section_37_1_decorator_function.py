# def super_secret_function(func):
#     return func
#
#
# def my_function():
#     print(f'this is "{my_function.__name__}" function')
#
#
# my_func = super_secret_function(my_function)
# my_func  # <function my_function at xxxxxxxxxxxx>
# my_func()  # this is "my_function" function
#
#
# @super_secret_function
# def my_function_2():
#     print(f"this is '{my_function_2.__name__}' function")
#
#
# my_function_2  # <function my_function_2 at xxxxxxxxxxxx>
# my_function_2()  # this is 'my_function_2' function
#

# def my_disabled_function(func):
#     """
#     This function returns nothing, and hence removes the decorated function
#     from the local scope.
#     """
#     pass
#
#
# @my_disabled_function
# def my_function_3():
#     print(f"this is '{my_function_3.__name__}' function")
#
#
# my_function_3  # None
# my_function_3()  # TypeError: 'NoneType' object is not callable

def print_args(func):
    def inner_func(*args, **kwargs):
        print(f'args : {args} | kwargs : {kwargs}')
        return func(*args, **kwargs)
    return inner_func


def multiply(num_a, num_b):
    print(f'num_a: {num_a} * num_b: {num_b} = {num_a * num_b}')


my_func = print_args(multiply)

my_func  # <function multiply at xxxxxxxxxxxx>
# my_func(2, 3)

