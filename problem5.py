# import math
from tools.primes import prime_factors_dict

def smallest_multiple(n):
    result_factors = {}

    for i in range(1, n+1):
        factors = prime_factors_dict(i)
        for key in factors:
            if key in result_factors:
                result_factors[key] = max(result_factors[key], factors[key])
            else:
                result_factors[key] = factors[key]

    r = 1
    for key in result_factors:
        r *= key ** result_factors[key]

    return r

if __name__ == '__main__':
    print(smallest_multiple(20))
