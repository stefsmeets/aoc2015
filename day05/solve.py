import argparse
from itertools import pairwise
from pathlib import Path

from helpers import timeit


DATA = Path(__file__).with_name('data.txt')


def cond1(s):
    return not any(a + b in ('ab', 'cd', 'pq', 'xy') for a, b in pairwise(s))


def cond2(s):
    return any(a == b for a, b in pairwise(s))


def cond3(s):
    return sum(c in 'aeiou' for c in s) >= 3


@timeit
def part1(s: str):
    lines = s.splitlines()

    total_nice = 0

    for line in lines:
        nice = cond1(line) and cond2(line) and cond3(line)
        total_nice += nice

    return total_nice


def cond4(s):
    pairs = {}

    for i, pair in enumerate(pairwise(s)):
        if pair in pairs and (i - pairs[pair] > 1):
            return True

        pairs.setdefault(pair, i)

    return False


def cond5(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True

    return False


@timeit
def part2(s: str):
    lines = s.splitlines()

    total_nice = 0

    for line in lines:
        nice = cond4(line) and cond5(line)
        total_nice += nice

    return total_nice


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--parts', nargs='+', type=int,
        choices=(1, 2), default=(1, 2))
    parser.add_argument('data', nargs='?', default=DATA)
    args = parser.parse_args()

    data = Path(args.data).read_text()

    for i in args.parts:
        func = (..., part1, part2)[i]
        func(data)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
