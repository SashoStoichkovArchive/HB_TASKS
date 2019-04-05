def accepts(*args):
    def accepter(func):
        def decorated(*arg):
            for index, argv in enumerate(args):
                if argv != type(arg[index]):
                    print("TypeError: Argument {} of {} is not {}!".format(index+1, func.__name__, argv.__name__))
        return decorated
    return accepter

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

# say_hello("Pesho")
say_hello(1)

@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

# deposit("Roza", 1)
# deposit("Roza", "a")