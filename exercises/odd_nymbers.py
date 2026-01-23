def get_odd_sum(numbers):
    res = sum([item for item in numbers if not item % 2])
    
    return res

# print(get_odd_sum([2,5,88,99,21,56, 43, 5, 88, 13, 23, 21] ))

# Вывеcти комбинации всех значений из трёх листов