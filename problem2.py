def fib():
    a = 1
    b = 1
    yield a
    yield b

    while True:
        (a, b) = (b, a+b)
        yield b

sum = 0
for f in fib():
    if f > 4000000:
        break

    if f % 2 == 0:
        sum += f

print(sum)
