from tools.primes import is_prime


def get_rotations(n):
    lst = list(str(n))

    seen = set()

    for i in range(len(lst)):
        x = int(''.join(lst[i:]+lst[:i]))
        if x not in seen:
            seen.add(x)
            yield x


def is_circular_prime(n):
    for x in get_rotations(n):
        if not is_prime(x):
            return False
    return True


def circular_primes(max):
    return len([
        n
        for n in range(3, max, 2)
        if is_circular_prime(n)
    ]) + 1


def run():
    return circular_primes(1000000)
