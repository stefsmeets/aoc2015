import argparse
import hashlib
from itertools import count
from pathlib import Path

from helpers import timeit


DATA = Path(__file__).with_name('data.txt').read_text()


def solve(s, *, prefix):
    string = s.splitlines()[0]

    for i in count():
        m = hashlib.md5(f'{string}{i}'.encode())
        h = m.hexdigest()
        if h.startswith(prefix):
            break

    return i


@timeit
def part1(s: str):
    return solve(s, prefix='00000')


@timeit
def part2(s: str):
    return solve(s, prefix='000000')


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
