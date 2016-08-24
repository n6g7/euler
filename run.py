#!/usr/bin/env python3
import math

def run_problem(n):
    level = math.ceil(n /25)
    level_package = 'solutions.level%s' % level

    problem = __import__('%s.problem%s' % (level_package, n), fromlist=(level_package))

    print(problem.run())

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Runs a Project Euler solution')
    parser.add_argument('number', type=int, help='The number of the problem')

    args = parser.parse_args()
    run_problem(args.number)
