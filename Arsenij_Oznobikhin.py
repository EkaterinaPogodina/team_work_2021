def Valid(f, numbers):
    for number in numbers:
        if type(number) != int and type(number) != float:
            print('Wrong data')
            return None
    return f(numbers)


@Valid()
def CountSum(numbers):
    return sum(numbers)


@Valid()
def CountProd(numbers):
    prod = 1
    for number in numbers:
        prod *= number
    return prod
