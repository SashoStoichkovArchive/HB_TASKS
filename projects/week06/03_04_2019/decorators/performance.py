import time, datetime

def performance(filename):
    def accepter(func):
        def decorated(*args, **kwargs):
            start = time.time()
            func()
            end = time.time()
            file = open(filename, "a")
            file.write("{0} was called at {1} and took {2:.2f} seconds to complete\n".format(func.__name__, datetime.datetime.now(), (end - start)))
        return decorated
    return accepter

@performance('log2.txt')
def heavy():
    time.sleep(3.14)

    print("I am done")

heavy()