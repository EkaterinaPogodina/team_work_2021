def summa(a, b):
    c = a + b
    return c


def elevate(a, n):
    c = a ** n
    return c


def decor(funct):
    import time
    start = time.time()
    funct()
    end = time.time()
    print(end - start)
    return funct()


a = int(input())
b = int(input())
c = int(input())
d = int(input())
decor(summa(a, b))
decor(elevate(c, d))
