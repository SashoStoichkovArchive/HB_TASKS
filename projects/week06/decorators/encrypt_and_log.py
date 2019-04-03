import datetime
from functools import wraps

def encrypt(num):
    def accepter(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            encrypted_string = ""
            for ch in func():
                if ch != " ":
                    char = chr(ord(ch) + num)
                    encrypted_string += char
                else:
                    encrypted_string += ch                    
            return encrypted_string
        return decorated
    return accepter

def log(filename):
    def accepter(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            file = open(filename, "a")
            file.write("{} was called at {}\n".format(func.__name__, datetime.datetime.now()))
            file.close()
            return func(*args, **kwargs)
        return decorated
    return accepter

@log("log.txt")
@encrypt(2)
def get_low():
    return "Get get get low"

print(get_low())