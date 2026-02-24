l1 = [2,3,4,1,2,5,6,2,1,7,4,8]

n = len(l1)
swapped = False

for i in range(n):
    for j in range(n - i - 1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]
            swapped = True
    
    if not swapped:
        break

print(l1)
print(sorted(l1))