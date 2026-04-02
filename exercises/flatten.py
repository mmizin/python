
def flatten(l: list) -> list:
    result = []
    for item in l:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
            
    return result


l1 = [1, [2, [3, 4], 5]]
print(flatten(l1))

def new_flatten(l: list) -> list:
    result = []
    stack = l1

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            result.append(item)

    return result[::-1]

print(new_flatten(l1))