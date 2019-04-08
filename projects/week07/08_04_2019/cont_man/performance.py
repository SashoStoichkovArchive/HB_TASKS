from contextlib import contextmanager
import time, datetime

@contextmanager
def performance(filename):
    f = open(filename, "a")
    start = time.time()

    yield

    end = time.time()
    f.write("Date {0}. Execution time: {1}".format(datetime.datetime.now(), end-start))
    f.close()


with performance('log.txt'):
    time.sleep(3.14)