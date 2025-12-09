from aoc.utils import read_lines


def part1(lines):
    sum = 0
    for line in lines:
        first, second = 0, 1
        for i in range(1, len(line)):
            if int(line[first]) < int(line[i]) and i != len(line) - 1:
                first = i
                second = i + 1
            elif int(line[second]) < int(line[i]):
                second = i
        sum += int(line[first] + line[second])
    return sum


def part2(lines):
    sum = 0
    for line in lines:
        positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        for pos in range(len(positions)):
            start = 0 if pos == 0 else positions[pos - 1] + 1
            positions[pos] = start
            for i in range(
                start,
                len(line) - len(positions) + pos + 1,
            ):
                if int(line[positions[pos]]) < int(line[i]):
                    positions[pos] = i

        num = ""
        for pos in positions:
            num += line[pos]
        sum += int(num)
    return sum


if __name__ == "__main__":
    lines = read_lines(3)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
