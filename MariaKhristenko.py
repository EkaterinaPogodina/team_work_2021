from datetime import datetime


def print_function(f):
    def function_wrapper(*args):
        print(datetime.now())
        output = f(*args)
        print(datetime.now())
        return output
    return function_wrapper


@print_function
def sum_of_two_numbers(first_value, second_value):
    return first_value + second_value


@print_function
def power(first_value, second_value):
    return first_value**second_value
