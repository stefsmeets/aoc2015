from pathlib import Path


def part1(s: str):
    line = s.splitlines()[0]

    level = 0

    for c in line:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        else:
            raise ValueError(c)

    return level


def part2(s: str):
    line = s.splitlines()[0]

    level = 0

    for i, c in enumerate(line):
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        else:
            raise ValueError(c)

        if level == -1:
            break

    return i + 1


if __name__ == '__main__':
    DATA = Path(__file__).with_name('data.txt')

    print(part1(DATA))
    print(part2(DATA))
