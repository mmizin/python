def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd


gen = odds(3, 21)
next(gen)
next(gen)
next(gen)
print(f"Next gen = {next(gen)}")

for i in gen:
    print(f'Generator in for loop, continue next(gen) = {next(gen)}')

gen2 = odds(7, 78)
print(f'We can write everything from generator in the list: {list(gen2)}')