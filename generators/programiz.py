# https://www.programiz.com/python-programming/generator

def two_yield():
    c = 10
    n = 1
    while True:
        yield n, c
        n += 1
        c += 1


res = two_yield()

# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))


class PawTwo:

    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result


paw = PawTwo(3)

# print(next(paw))
# print(next(paw))
# print(next(paw))
# print(next(paw))
# print(next(paw))  # StopIteration


def paw_two(max=0):
    count = 0
    while count < max:
        yield 2 ** count
        count += 1


paw_func = paw_two(3)

# print(next(paw_func))
# print(next(paw_func))
# print(next(paw_func))
# print(next(paw_func)) # StopIteration

# for num in paw_two(3):
#     print(num)


def foo(l):
    l.append('test')


lis = [1]

foo(lis)

print(lis)

