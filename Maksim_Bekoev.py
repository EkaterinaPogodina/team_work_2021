import time


def time_counting(f):
    def wrapper(*args):
        start = time.time()
        result = f(*args)
        print(time.time() - start)
        return result
    return wrapper


@time_counting
def my_sum(x, y):
    return x + y


@time_counting
def my_pow(x, y):
    return x**y