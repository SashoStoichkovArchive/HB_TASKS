import time

def performance(filename):
    def accepter(func):
        def decorated(*args, **kwargs):
            start = time.time()
            func()
            end = time.time()
            file = open(filename, "a")
            file.write("{0} was called and took {1:.2f} seconds to complete\n".format(func.__name__, (end - start)))
        return decorated
    return accepter

@performance('log2.txt')
def heavy():
    time.sleep(3.14)

    print("I am done")

heavy()