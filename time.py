#!/usr/bin/env python3
from cli.run import run_problem, problem_exists
from time import time

MAX_LINE = 15


def time_solution(n):
    start = time()
    run_problem(n)
    return time() - start


def format_line(n, t):
    head = ('Problem %s:' % n).ljust(11)

    if t > 1:
        t2 = round(t, 3)
        unit = 's'
    else:
        t2 = round(t * 1000, 1)
        unit = 'ms'

    tt = '[ %s %s ]' % (('%s' % t2).rjust(6), unit.ljust(2))

    line = '=' * round(t / MAX_LINE * 80)

    return '%s %s %s' % (head, tt, line)


def time_solutions():
    start = time()
    n = 1
    while problem_exists(n):
        print(format_line(n, time_solution(n)))
        n += 1

    duration = time() - start
    print('%s problems solved in %s seconds' % (n-1, round(duration, 1)))


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Times solutions')

    args = parser.parse_args()

    time_solutions()
