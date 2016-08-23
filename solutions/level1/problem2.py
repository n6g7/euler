def fibonacci():
    a = 1
    b = 1
    yield a
    yield b

    while True:
        (a, b) = (b, a+b)
        yield b

def sum_even_fibo(max):
    sum = 0

    for f in fibonacci():
        if f > max:
            break

        if f % 2 == 0:
            sum += f

    return sum

if __name__ == '__main__':
    n = 4000000
    print(sum_even_fibo(n))
