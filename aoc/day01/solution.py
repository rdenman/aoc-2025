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
        distance = int(line[1:])
        if line.startswith("L"):
            if pos == 0:
                count += distance // 100
            elif distance >= pos:
                count += (distance - pos) // 100 + 1
            pos = (pos - distance) % 100
        elif line.startswith("R"):
            count += (pos + distance) // 100
            pos = (pos + distance) % 100
    return count


if __name__ == "__main__":
    lines = read_lines(1)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
