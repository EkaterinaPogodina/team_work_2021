import string


def decorator_1(func):
    def lower_to_upper(*args):
        s = func(*args)
        return s.upper()
    return lower_to_upper


@decorator_1
def my_func_for_first_task(first_str, second_str):
    return first_str + second_str


def decorator_2(func):
    def delete_vowels(*args, list_of_letters=['A', 'E', 'I', 'O', 'U', 'Y']):
        s = func(*args)
        for i in list_of_letters:
            s = s.replace(i, '')
        return s.upper()
    return delete_vowels


@decorator_2
def my_func_for_second_task(str_):
    return str_.upper()
