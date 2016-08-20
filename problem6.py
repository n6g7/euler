def squares_difference(n):
    if n == 1:
        return 0

    return squares_difference(n-1) + 2*n*sum(range(1, n))

if __name__ == '__main__':
    print(squares_difference(100))
