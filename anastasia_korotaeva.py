def turnaround(func):
    """turns two strings around"""
    def wrapper(el1, el2):
        el1_new = el1[::-1]
        el2_new = el2[::-1]
        return func(el1_new, el2_new)
    return wrapper



@turnaround
def numbers(str1, str2):
    """two inversed numbers sum"""
    return int(str1) + int(str2)


@turnaround
def strings(str1, str2):
    """two inversed strings sorted"""
    return sorted([str1, str2])


arg1, arg2 = input().split()
print(numbers(arg1, arg2))
print(*strings(arg1, arg2))
