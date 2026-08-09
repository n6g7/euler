#!/usr/bin/env python3
import sys

from cli.run import run_problem

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Runs a Project Euler solution')
    parser.add_argument('number', type=int, help='The number of the problem')

    args = parser.parse_args()

    answer, elapsed = run_problem(args.number)
    print(answer)

    t, unit = (elapsed, 's') if elapsed >= 1 else (elapsed * 1000, 'ms')
    msg = f'({round(t, 1)}{unit})\n'
    if sys.stderr.isatty():
        msg = f'\033[90m{msg}\033[0m'
    sys.stderr.write(msg)
