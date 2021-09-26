def to_upper(func):
    def wrapper(*args):
        res = func(*args)
        return res.upper()

    return wrapper


@to_upper
def concatenate_strings(string_1, string_2):
    return string_1 + string_2


@to_upper
def delete_all_vowels(string):
    res = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for char in string:
        if char not in vowels:
            res += char
    return res
