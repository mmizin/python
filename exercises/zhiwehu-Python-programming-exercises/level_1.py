import math

# Question 1
# Level 1
#
# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method

print('Answer on Question 1:')
print(*[i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0], sep=',')

# Question 2
# Level 1
#
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
num = 8

print('\nAnswer on Question 2:')
print(math.factorial(num))

fact_num = 1
for i in range(num, 0, -1):
    fact_num *= i
print(fact_num)


def get_fact(number):
    if number == 1:
        return number
    else:
        return number * get_fact(number-1)


print(get_fact(num))

# Question 3
# Level 1
#
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()

num = 8
print('\nAnswer on Question 3:')
print({k: k*k for k in range(1, num+1)})

print(dict(zip([k for k in range(1, num+1)], [v*v for v in range(1, num+1)])))

# Question 4
# Level 1
#
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

inp = '34,67,55,33,12,98'

print('\nAnswer on Question 4:')
print(inp.split(','))
print(tuple(inp.split(',')))

# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also, please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters


class GetPrintStr:

    def __init__(self):
        self.text = None

    @property
    def get_string(self):
        # self.text = input('Enter the text: ')
        pass

    @property
    def print_string(self):
        if self.text:
            print(self.text.upper())


print('\nAnswer on Question 5: Enable line 111 to see the result.')
get_print_str = GetPrintStr()

get_print_str.get_string
get_print_str.print_string


