from pathlib import Path


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


def part2(s: str):
    lines = s.splitlines()

    ribbon = 0

    for line in lines:
        s1, s2, s3 = sorted(tuple(int(val) for val in line.split('x')))

        wrap = (s1 + s2) * 2
        bow = s1 * s2 * s3

        ribbon += wrap + bow

    return ribbon


if __name__ == '__main__':
    DATA = Path(__file__).with_name('data.txt')

    print(part1(DATA))
    print(part2(DATA))
