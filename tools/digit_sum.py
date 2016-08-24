def digit_sum(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s
