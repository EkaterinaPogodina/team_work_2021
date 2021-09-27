import time


def main_function(f):
    def wrapper(x, y):
        start_time = time.time()
        ans = f(x, y)
        end_time = time.time()
        run_time = end_time - start_time
        a = ['секунд', 'миллисекунд', 'микросекунд']
        s = ''
        for i in range(3):
            s += str(int(run_time)) + " " + a[i] + " "
            run_time = (run_time % 1) * 1000
        print(s)
        return ans

    return wrapper


@main_function
def summa(x, y):
    return x + y


@main_function
def stepen(x, y):
    return x ** y
