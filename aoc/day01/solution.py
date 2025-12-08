from aoc.utils import read_lines


def part1(lines):
    count = 0
    pos = 50
    for line in lines:
        if line.startswith("L"):
            pos = (pos - int(line[1:])) % 100
        elif line.startswith("R"):
            pos = (pos + int(line[1:])) % 100
        if pos == 0:
            count += 1
    return count


def part2(lines):
    count = 0
    pos = 50
    for line in lines:
        if line.startswith("L"):
            pos = pos - int(line[1:])
        elif line.startswith("R"):
            pos = pos + int(line[1:])
        if pos == 0:
            count += 1
        elif pos > 99:
            while pos > 99:
                pos -= 100
                count += 1
        elif pos < 0:
            while pos < 0:
                pos += 100
                count += 1
    return count


if __name__ == "__main__":
    lines = read_lines(1)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
