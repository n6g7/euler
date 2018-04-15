from tools.sequence.fibonacci import fibonacci


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
