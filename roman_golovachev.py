def check(f):
    def wrapper(nums):
        ok = True
        for i in range(len(nums)):
            if type(nums[i]) != type(0):
                ok = False
        if not ok or len(nums) == 0:
            print("Wrong data")
            return None
        return f(nums)
    return wrapper

@check
def product(nums):
    product_ = 1
    for i in range(len(nums)):
        product_ *= nums[i]
    return product_

@check
def sum(nums):
    sum_ = 0
    for i in range(len(nums)):
        sum_ += nums[i]
    return sum_
