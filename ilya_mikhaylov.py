def upper_case(f):
    def wrapper(*args):
        return f(*args).upper()
    return wrapper


@upper_case
def concatination(str1, str2):
    return str1 + str2


@upper_case
def delete_vowel(string: str) -> str:
    return string.lower()\
        .replace('a', '')\
        .replace('e', '')\
        .replace('u', '')\
        .replace('i', '')\
        .replace('o', '')
