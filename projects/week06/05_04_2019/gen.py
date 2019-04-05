# generator

def odd_numbers():
    start = 1
    while start < 20:
        yield start
        start += 2
        print("===")
        yield 1

gen = odd_numbers()

for el in gen:
    print("bet el")
    print(el)