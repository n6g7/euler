from .primes import prime_factors_dict

def count_divisors(n):
    if n == 1:
        return 1

    count = 1
    factors = prime_factors_dict(n)

    for factor in factors:
        count *= factors[factor] + 1

    return count
