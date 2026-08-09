def squares_difference(n):
    if n == 1:
        return 0

    return squares_difference(n-1) + 2*n*sum(range(1, n))


def run():
    return squares_difference(100)


if __name__ == '__main__':
    print(run())
