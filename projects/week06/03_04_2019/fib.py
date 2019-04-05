class Fib:
    def __init__(self):
        self.state = [1, 1]

    def __call__(self):
        curr_num = self.state[-1] + self.state[-2]
        self.state.append(curr_num)

        return curr_num

f = Fib()
print(f())
print(f())
print(f())
print(f())
