#!/usr/bin/env python3
from cli.run import run_problem

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Runs a Project Euler solution')
    parser.add_argument('number', type=int, help='The number of the problem')

    args = parser.parse_args()
    print(run_problem(args.number))
