def compress(iterable, mask):
    i1 = iter(iterable)
    i2 = iter(mask)

    while True:
        try:
            if next(i2) == True:
                yield next(i1)
            else:
                next(i1)
        except StopIteration:
            break

    return iterable

print(list(compress(["Ivo", "Rado", "Panda"], [True, False, True])))
print(list(compress(["Ivo", "Rado", "Panda"], [False, True, False])))
print(list(compress(["Ivo", "Rado", "Panda"], [False, False, False])))
print(list(compress(["Ivo", "Rado", "Panda"], [True, True, True])))
