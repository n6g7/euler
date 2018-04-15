from tools.primes import is_prime


def get_truncatures(n):
    lst = list(str(n))

    yield n
    for i in range(1, len(lst)):
        yield int(''.join(lst[i:]))
        yield int(''.join(lst[:-i]))


def is_truncatale_prime(n):
    for trunc in get_truncatures(n):
        if not is_prime(trunc):
            return False
    return True


def truncatable_primes(limit):
    primes = []
    n = 11

    while len(primes) < limit:
        if is_truncatale_prime(n):
            primes.append(n)
        n += 2

    return sum(primes)


def run():
    return truncatable_primes(11)
