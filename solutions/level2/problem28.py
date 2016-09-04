from tools.primes import is_prime, list_primes

def number_spiral_diags(size):
    if size == 1:
        return 1

    start = (size-2) ** 2
    return 4 * start + 10 * (size-1) + number_spiral_diags(size-2)

def run():
    return number_spiral_diags(1001)
