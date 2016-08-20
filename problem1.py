def sum_multiples(max):
    multiples = set(range(0, max, 3)) | set(range(0, max, 5))

    return sum(multiples)

if __name__ == '__main__':
    n = 1000
    print(sum_multiples(n))
