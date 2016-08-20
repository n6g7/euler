import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.floor(math.sqrt(n))

    for x in range(3, root+1, 2):
        if n % x == 0:
            return False

    return True

def prime_factors(n, reverse=False):
    root = math.floor(math.sqrt(n))

    for x in range(2, root+1):
        if n % x == 0 and is_prime(x):

            if not reverse:
                yield x
            for y in prime_factors(int(n / x), reverse):
                yield y
            if reverse:
                yield x

            return
    yield n
