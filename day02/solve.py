import argparse
import os
from pathlib import Path

import numpy as np

from helpers import timeit


DATA = Path(__file__).with_name('data.txt').read_text()


@timeit
def part1(s: str):
    lines = s.splitlines()

    paper = 0

    for line in lines:
        w, h, l = (int(val) for val in line.split('x'))
        sides = (w * h, h * l, w * l)
        smallest = min(sides)

        total = sum(sides) * 2 + smallest

        paper += total

    return paper


@timeit
def part2(s: str):
    lines = s.splitlines()

    ribbon = 0

    for line in lines:
        s1, s2, s3 = sorted(tuple(int(val) for val in line.split('x')))

        wrap = (s1 + s2) * 2
        bow = s1 * s2 * s3

        ribbon += wrap + bow

    return ribbon


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
