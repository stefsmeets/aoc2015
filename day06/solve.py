from pathlib import Path

import numpy as np


def solve(s: str, *, f_on, f_off, f_toggle, dtype):
    lines = s.splitlines()

    lights = np.zeros((1000, 1000), dtype=dtype)

    for line in lines:
        match line.split():
            case 'turn', 'on', start, _, stop:
                f = f_on
            case 'turn', 'off', start, _, stop:
                f = f_off
            case 'toggle', start, _, stop:
                f = f_toggle

        x1, y1 = (int(val) for val in start.split(','))
        x2, y2 = (int(val) for val in stop.split(','))

        lights[x1:x2 + 1, y1:y2 + 1] = f(lights[x1:x2 + 1, y1:y2 + 1])

    return int(lights.sum())


def part1(s: str):
    return solve(s,
                 f_on=lambda x: True,
                 f_off=lambda x: False,
                 f_toggle=lambda x: ~x,
                 dtype=bool)


def part2(s: str):
    return solve(s,
                 f_on=lambda x: x + 1,
                 f_off=lambda x: np.fmax(0, x - 1),
                 f_toggle=lambda x: x + 2,
                 dtype=int)


if __name__ == '__main__':
    DATA = Path(__file__).with_name('data.txt')

    print(part1(DATA))
    print(part2(DATA))
