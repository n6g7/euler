from tools.primes import list_primes


def nth_prime(n):
    counter = 0
    for x in list_primes():
        counter += 1

        if counter == n:
            return x


def run():
    return nth_prime(10001)
