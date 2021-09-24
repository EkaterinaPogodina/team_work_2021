def to_upper(func):
    def wrapper(*args):
        res = func(*args)
        return res.upper()

    return wrapper


@to_upper
def concatenate_strings(string_1, string_2):
    string_1 += string_2
    all_chars = []
    for char in string_1:
        all_chars.append(char)
    res = ''.join(sorted(all_chars))
    return res


@to_upper
def delete_all_vowels(string):
    res = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for char in string:
        if char not in vowels:
            res += char
    return res
