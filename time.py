#!/usr/bin/env python3
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep, time

from cli.run import list_problems, run_problem

SPINNER = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'


def format_line(n, t, max_t):
    head = f'Problem {n}:'.ljust(11)
    t2, unit = (round(t, 3), 's') if t > 1 else (round(t * 1000, 1), 'ms')
    tt = f'[ {str(t2).rjust(6)} {unit.ljust(2)} ]'
    bar = '=' * round(t / max_t * 60)
    return f'{head} {tt} {bar}'


def _render(problems, results, frame):
    max_t = max(results.values(), default=1)
    sys.stdout.write(f'\033[{len(problems)}A')
    for n in problems:
        if n in results:
            line = format_line(n, results[n], max_t)
        else:
            line = f'Problem {n}:'.ljust(11) + f'  {SPINNER[frame % len(SPINNER)]}'
        sys.stdout.write(f'\r{line}\033[K\n')
    sys.stdout.flush()


def time_solutions(jobs=None):
    problems = list_problems()
    results = {}
    tty = sys.stdout.isatty()

    if tty:
        for n in problems:
            print(f'Problem {n}:'.ljust(11) + f'  {SPINNER[0]}')

    lock = threading.Lock()
    frame = [0]
    stop = threading.Event()

    def spin():
        while not stop.is_set():
            with lock:
                _render(problems, results, frame[0])
            frame[0] += 1
            sleep(0.08)

    if tty:
        threading.Thread(target=spin, daemon=True).start()

    start = time()
    with ThreadPoolExecutor(max_workers=jobs) as executor:
        futures = {executor.submit(run_problem, n): n for n in problems}
        for future in as_completed(futures):
            with lock:
                _, elapsed = future.result()
                results[futures[future]] = elapsed
    total = time() - start

    stop.set()

    if tty:
        with lock:
            _render(problems, results, frame[0])
    else:
        max_t = max(results.values(), default=1)
        for n in sorted(results):
            print(format_line(n, results[n], max_t))

    print(f'\n{len(problems)} problems solved in {round(total, 1)}s')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Times all solutions')
    parser.add_argument('-j', '--jobs', type=int, default=None,
                        help='parallel workers (default: auto)')
    args = parser.parse_args()

    time_solutions(jobs=args.jobs)
