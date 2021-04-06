# Decorator attaches new behaviors to the objects without modifying their structure.
# The pattern produces a decorator class to wrap the original one and add new functionality.
# Use case. Use the Decorator pattern each time I need to add extra behaviors to objects without getting into the code.

class MyDecorator:
    def __init__(self, func):
        print("Inside MyDecorator.__init__()")
        func()

    def __call__(self, *args, **kwargs):
        print('Inside MyDecorator.__call__')


@MyDecorator
def my_function():
    print('Inside my function()')


if __name__ == '__main__':
    my_function()
