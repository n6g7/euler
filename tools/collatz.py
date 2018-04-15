def collatz_next(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3 * n + 1


collatz_lengths = {
    1: 1
}


def collatz_length(n):
    if n not in collatz_lengths:
        collatz_lengths[n] = 1 + collatz_length(collatz_next(n))
    return collatz_lengths[n]
