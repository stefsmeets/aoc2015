from itertools import pairwise
from pathlib import Path


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


def part1(s: str):
    return solve(s, conditions=(cond1, cond2, cond3))


def part2(s: str):
    return solve(s, conditions=(cond4, cond5))


if __name__ == '__main__':
    DATA = Path(__file__).with_name('data.txt')

    print(part1(DATA))
    print(part2(DATA))
