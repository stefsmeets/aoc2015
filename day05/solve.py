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


def cond4(s):
    pairs = {}

    for i, pair in enumerate(pairwise(s)):
        if pair in pairs and (i - pairs[pair] > 1):
            return True
        pairs.setdefault(pair, i)

    return False


def cond5(s):
    return any(s[i - 2] == s[i] for i in range(2, len(s)))


def solve(s, conditions):
    lines = s.splitlines()
    return sum(all(cond(line) for cond in conditions) for line in lines)


@timeit
def part1(s: str):
    return solve(s, conditions=(cond1, cond2, cond3))


@timeit
def part2(s: str):
    return solve(s, conditions=(cond4, cond5))


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
