from tools.divisors import is_abundant

limit = 28123


def get_abundants(max):
    return frozenset(filter(is_abundant, range(max)))


def non_abundant_sums(limit):
    abundants = get_abundants(limit)
    candidates = set(range(limit+1))

    for i in abundants:
        for j in abundants:
            try:
                candidates.remove(i+j)
            except Exception:
                pass

    return sum(candidates)


def run():
    return non_abundant_sums(limit)
