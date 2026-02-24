from collections import Counter
l1 = ["e404", "e405", "e403", "e404","e404", "e404", "e404", "e405", "e403", "e405", "e403", "e403", "e403", "e403", "e403", "e405", "e405", "e405", "e402"]

counter = sorted(Counter(l1), key=l1.count)
print(counter)
print(counter[-2:])

counter = Counter(l1)
print([k[0] for k in counter.most_common(2)])

counter = Counter(l1)
sorted_counter = sorted(counter.items(), key=lambda item: item[1])
print([x[0] for x in sorted_counter[-2:]])