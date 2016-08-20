def brute(sum):
    for a in range(1, sum):
        for b in range(1, sum):
            c = sum - a - b

            if (a ** 2 + b ** 2) == c ** 2:
                return a*b*c

if __name__ == '__main__':
    print(brute(1000))
