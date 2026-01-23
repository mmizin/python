def fizz_buzz(n: int):
    result_l = []
    for i in range(1, n + 1):
        if not i % 3 and not i % 5:
            result_l.append('FizzBuzz')
        elif not i % 5:
            result_l.append('Buzz')
        elif not i % 3:
            result_l.append('Fizz')
        else:
            result_l.append(str(i))
    
    return result_l


print(fizz_buzz(5))  # ["1", "2", "Fizz", "4", "Buzz"]
print(fizz_buzz(15))


def fizz_buzz(n: int):
    return ['FizzBuzz' if not (i % 3 or i % 5) else "Fizz" if not i % 3 else "Buzz" if not i % 5 else f'{i}' for i in
            range(1, n + 1)]


print(fizz_buzz(5))  # ["1", "2", "Fizz", "4", "Buzz"]
print(fizz_buzz(15))
