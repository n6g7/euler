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

def run():
    return sum_even_fibo(4000000)
