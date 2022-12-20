import hashlib
from itertools import count
from pathlib import Path


def solve(s, *, prefix):
    string = s.splitlines()[0]

    for i in count():
        m = hashlib.md5(f'{string}{i}'.encode())
        h = m.hexdigest()
        if h.startswith(prefix):
            break

    return i


def part1(s: str):
    return solve(s, prefix='00000')


def part2(s: str):
    return solve(s, prefix='000000')


if __name__ == '__main__':
    DATA = Path(__file__).with_name('data.txt').read_text()

    print(part1(DATA))
    print(part2(DATA))
