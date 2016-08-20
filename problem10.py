from tools.primes import list_primes

def sum_primes(threshold):
    sum = 0
    for n in list_primes():
        if n > threshold:
            break

        sum += n

    return sum

if __name__ == '__main__':
    print(sum_primes(2000000))
