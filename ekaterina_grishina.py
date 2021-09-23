def is_right_data(f):
    def is_it_right(lst):
        if len(lst) == 0:
            print("Wrong data")
            return None
        for i in lst:
            if type(i) != int and type(i) != float:
                print("Wrong data")
                return None
        return f(lst)

    return is_it_right


@is_right_data
def sum_list(lst):
    result = 0
    for i in lst:
        result += i
    return result


@is_right_data
def product_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result


a = [1, 2, "a"]
print(product_list(a))
