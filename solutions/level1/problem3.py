from tools.primes import prime_factors

def largest_prime_factor(n):
    for x in prime_factors(n, reverse=True):
        return x

def run():
    return largest_prime_factor(600851475143)
