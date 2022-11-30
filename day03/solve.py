import argparse
import os
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from helpers import timeit


DATA = Path(__file__).with_name('data.txt').read_text()


@timeit
def part1(s: str):
    line = s.strip()

    x, y = (0, 0)

    houses = defaultdict(int)
    houses[x, y] += 1

    for char in line:
        match char:
            case '<':
                x -= 1
            case '>':
                x += 1
            case '^':
                y += 1
            case 'v':
                y -= 1

        houses[x, y] += 1

    return len(houses)


class Point:
    x: int = 0
    y: int = 0


@timeit
def part2(s: str):
    line = s.strip()

    current, other = Point(), Point()

    houses = defaultdict(int)
    houses[current.x, current.y] += 2

    for char in line:
        match char:
            case '<':
                current.x -= 1
            case '>':
                current.x += 1
            case '^':
                current.y += 1
            case 'v':
                current.y -= 1

        houses[current.x, current.y] += 1

        current, other = other, current

    return len(houses)


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
