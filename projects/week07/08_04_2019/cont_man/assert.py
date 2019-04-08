class assertRaises:
    def __init__(self, expected_exc, msg=None):
        self.expected_exc = expected_exc

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is None:
            print("{0} was not raised".format(self.expected_exc.__name__))
        elif isinstance(exc_value, self.expected_exc):
            print("{0} was raised Success!".format(self.expected_exc.__name__))
        print("{0} was raised Fail!".format(exc_type.__name__))
        return True

def do_something():
    arr = [1, 2, 3]
    arr[3]

with assertRaises(TypeError):
    do_something()