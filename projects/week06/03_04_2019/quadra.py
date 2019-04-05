def quadra(a, b, c):
    def calc(x):
        return (a * x ** 2) + (b * x) + c
    return calc

func = quadra(1, 2, 3)

# print(func)
print(func(1))
print(func(2))
print(func(3))
