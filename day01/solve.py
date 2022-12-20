from pathlib import Path


def part1(s: str):
    line = s.splitlines()[0]

    up = sum(c == '(' for c in line)
    down = len(line) - up

    return up - down


def part2(s: str):
    line = s.splitlines()[0]

    level = 0

    for i, c in enumerate(line):
        level += +1 if c == '(' else -1

        if level == -1:
            break

    return i + 1


if __name__ == '__main__':
    DATA = Path(__file__).with_name('data.txt').read_text()

    print(part1(DATA))
    print(part2(DATA))
