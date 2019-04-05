def cycle(iterable):
    while True:
        for el in iterable:
            yield el

endless = cycle(range(1, 4))

for el in endless:
    print(el)