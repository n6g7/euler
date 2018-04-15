from tools.primes import is_prime, list_primes


def quadratic_score(a, b):
    n = 0
    while is_prime((n**2) + (a*n) + b):
        n += 1
    return n


def quadratic_primes(limit):
    # (Case n=0) b has to be prime.
    # Here are the possible values for b:
    primes_under_limit = []
    for n in list_primes():
        if n > limit:
            break
        primes_under_limit.append(n)

    max_primes = 0
    max_couple = ()

    for b in primes_under_limit:
        for a in range(-limit+1, limit):
            # (Case n=1) 1+a+b has to be a prime
            if not is_prime(1+a+b):
                continue

            score = quadratic_score(a, b)
            if score > max_primes:
                max_couple = (a, b)
                max_primes = score

    return max_couple[0] * max_couple[1]


def run():
    return quadratic_primes(1000)
