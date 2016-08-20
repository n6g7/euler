from tools.primes import prime_factors

def largest_prime_factor(n):
    for x in prime_factors(n, reverse=True):
        return x

if __name__ == '__main__':
    n = 600851475143
    print(largest_prime_factor(n))
