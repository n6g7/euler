import math
from .primes import prime_factors_dict

def count_divisors(n):
    if n == 1:
        return 1

    count = 1
    factors = prime_factors_dict(n)

    for factor in factors:
        count *= factors[factor] + 1

    return count

def get_divisors(n, proper=False):
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            if not proper or i != n:
                yield i

            o = int(n/i)
            if i != o:
                if not proper or o != n:
                    yield o

def sum_divisors(n, proper=False):
    return sum(get_divisors(n, proper))

def is_perfect(n):
    return sum_divisors(n, proper=True) == n

def is_deficient(n):
    return sum_divisors(n, proper=True) < n

def is_abundant(n):
    return sum_divisors(n, proper=True) > n
