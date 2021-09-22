import time


def calculate_time(f):
    def function_wrapper(*args):
        start_time = time.time()
        answer = f(*args)
        end_time = time.time()
        print('Program time is {} seconds.'.format(end_time - start_time))
        return answer
    return function_wrapper


@calculate_time
def sum_of_two(first, second):
    return first + second


@calculate_time
def exponentiation(number, value):
    return number**value
