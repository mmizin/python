import math

# Level 2
#
# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
#
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.

C = 50
H = 30
D = 40

QQQ = round(math.sqrt(2 * C * D / H))

print('\nAnswer on Question 6:')
print(QQQ)

# Question 7
# Level 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

inp = '3,5'
x, y = list(map(lambda i: int(i), inp.split(',')))

print('\nAnswer on Question 7:')
print([[i * j for j in range(y)] for i in range(x)])

# Question 8
# Level 2
#
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

text = 'without,hello,bag,world'

print('\nAnswer on Question 8:')
print(*sorted(text.split(',')), sep=',')

# Question 9
# Level 2
#
# Question£º
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

text = ['Hello world', 'Practice makes perfect']

print('\nAnswer on Question 9:')
while True:  # suppose we are getting text from the input
    for line in text:
        print(line.upper())
    break

# Question 10
# Level 2
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

text = 'hello world and practice makes perfect and hello world again'

remove_dup = set(text.split())

print('\nAnswer on Question 10:')
print(*sorted(remove_dup, reverse=False))

# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

b_numbers = '0100,0011,1010,1001'.split(',')

res = []
for n in b_numbers:
    t = int(n, 2)
    if not t % 5:
        res.append(n)

print('\nAnswer on Question 11:')
print(*res)
print(*[n for n in b_numbers if not int(n, 2) % 5])

# Question 12
# Level 2
#
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

numbers = [str(num) for num in range(1000, 3001)]
res = []

for num in numbers:
    odd_present = [True for char in num if int(char) % 2]
    if not odd_present:
        res.append(int(num))

print('\nAnswer on Question 12:')
print(*res, sep=',')

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

text = 'hello world! 123'

res = [len([c for c in text if c.isalpha()]), len([j for j in text if j.isdigit()])]

print('\nAnswer on Question 13:')
print(f'LETTERS {res[0]}\nDIGITS {res[1]}')

# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

text = 'Hello world!'

print('\nAnswer on Question 14:')
res = [len([upp_c for upp_c in text if upp_c.isupper()]), len([low_c for low_c in text if low_c.islower()])]
print(f'UPPER CASE {res[0]}\nLOWER CASE {res[1]}')

# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

number = '9'
mult = 4
res = 0
for c in range(1, mult + 1):
    res += int(number * c)
print('\nAnswer on Question 15:')
print(res)

# Question 16
# Level 2
#
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

numbers = '1,2,3,4,5,6,7,8,9'.split(',')
res = [num for num in numbers if int(num) % 2]

print('\nAnswer on Question 16:')
print(*res, sep=',')

# Question 17
# Level 2
#
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

data = 'D 300 D 300 W 200 D 100'.split()
d_data = {'D': [], 'W': []}

for c, d in enumerate(data):
    if d == 'D':
        d_data['D'].append(int(data[c + 1]))
    elif d == 'W':
        d_data['W'].append(int(data[c + 1]))

print('\nAnswer on Question 17:')
print(sum(d_data['D']) - sum(d_data['W']))
