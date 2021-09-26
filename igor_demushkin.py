import time


def main_function(f):
    def wrapper(x, y):
        start_time = time.time()
        ans = f(x, y)
        end_time = time.time()
        print(start_time - end_time)
        return ans

    return wrapper


@main_function
def summa(x, y):
    return x + y


@main_function
def stepen(x, y):
    return x ** y
