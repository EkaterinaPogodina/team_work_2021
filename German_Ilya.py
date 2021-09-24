import string


def decorator(func):
    def lower_to_upper(*args):
        return func(*args).upper()

    return lower_to_upper


@decorator
def plus_func(first, second):
    return first + second


@decorator
def delete_vowels(str_, list_of_letters=['A', 'E', 'I', 'O', 'U', 'Y' \
                                         'a', 'e', 'i', 'o', 'u', 'y']):
    for i in list_of_letters:
        str_ = str_.replace(i, '')
    return str_
