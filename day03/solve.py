from collections import defaultdict
from pathlib import Path


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


if __name__ == '__main__':
    DATA = Path(__file__).with_name('data.txt')

    print(part1(DATA))
    print(part2(DATA))
