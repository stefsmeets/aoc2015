import argparse
import os
from pathlib import Path

import numpy as np

from helpers import timeit


DATA = Path(__file__).with_name('data.txt').read_text()


@timeit
def part1(s: str):
    line = s.splitlines()[0]

    level = 0

    for c in line:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        else:
            raise ValueError(c)

    return level


@timeit
def part2(s: str):
    line = s.splitlines()[0]

    level = 0

    for i, c in enumerate(line):
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        else:
            raise ValueError(c)

        if level == -1:
            break

    return i + 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--parts', nargs='+', type=int,
        choices=(1, 2), default=(1, 2))
    parser.add_argument('data', nargs='?', default=DATA)
    args = parser.parse_args()

    for i in args.parts:
        func = (..., part1, part2)[i]
        func(args.data)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
