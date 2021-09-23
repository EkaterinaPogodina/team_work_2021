def mirror_inputs(func):
    """try to make inputs strings, mirror them and change back to the original type
    WARNING : don't use untrusted data types"""

    def wrapper(*args, **kwargs):
        try:
            args = list(args) #originally they're tuple which is a problem
            for i in range(len(args)):
                var = args[i]
                original_type = type(var)
                args[i] = original_type(str(var)[::-1])

            for kname, kvar in kwargs.items():
                original_type = type(kvar)
                kwargs[kname] = original_type(str(kvar)[::-1])
        except:
            raise ValueError("input arguments can't be mirrored as strings")

        return func(*args, **kwargs)

    return wrapper


@mirror_inputs
def return_sum(a: int, b: int):
    """на вход два числа, переворачивает их задом наперед и возвращает сумму эти чисел"""
    return a + b


@mirror_inputs
def order_strings(f_str: str, s_str: str):
    """на вход две строки, переворачивает их и печетает в отсортированном виде"""
    return sorted([f_str, s_str])


if __name__ == "__main__":
    print(return_sum(123, 567))
    print(return_sum(123, b = 567))
    print(order_strings("abc", "cde"))
    print(order_strings("abc", s_str = "cde"))
