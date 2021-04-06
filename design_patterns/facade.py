# Facade provides a simplified yet limited interface to decrease the complexity of an application.
# Complex subsystems with multiple moving parts could be “masked” by Facade.
# Use case. I create the Facade class in case I have to work with complex libraries & APIs and/
# or I need only the part of their functionality

class Addition:
    def __init__(self, field1: int, field2: int):
        self.field1 = field1
        self.field2 = field2

    def get_result(self):
        return self.field1 + self.field2


class Multiplication:
    def __init__(self, field1: int, field2: int):
        self.field1 = field1
        self.field2 = field2

    def get_result(self):
        return self.field1 * self.field2


class Facade:
    @staticmethod
    def make_addition(*args):
        return Addition(*args)

    @staticmethod
    def multiplication(*args):
        return Multiplication(*args)


if __name__ == '__main__':
    addition = Facade.make_addition(3, 3).get_result()
    multiplication = Facade.multiplication(3, 3).get_result()
    print(addition)
    print(multiplication)
