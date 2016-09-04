import math

def get_digits(n):
    order = math.floor(math.log10(n))
    for i in range(order+1):
        yield (n // (10 ** i)) % 10

def sum_digits(n, p=1):
    return sum([d ** p for d in get_digits(n)])
