def triangle_numbers():
    sum = 0
    n = 1
    while True:
        sum += n
        n += 1
        yield sum
