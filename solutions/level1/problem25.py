from tools.sequence.fibonacci import fibonacci

def n_digit_fib(n):
    limit = 10 ** (n-1)
    for (idx, i) in enumerate(fibonacci()):
        if i >= limit:
            return idx+1

def run():
    return n_digit_fib(1000)
