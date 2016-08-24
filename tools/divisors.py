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

def get_divisors(n):
    for i in range(1, math.ceil(n/2)+1):
        if n % i == 0:
            yield i

def sum_divisors(n):
    return sum(get_divisors(n))
