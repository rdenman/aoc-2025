from aoc.utils import read_lines


def parse_input(lines):
    ranges = []
    ids = None
    for line in lines:
        if ids != None:
            ids.append(int(line))
        elif line == "":
            ids = []
        else:
            ranges.append(line)
    return ranges, ids


def part1(lines):
    ranges, ids = parse_input(lines)
    fresh_ids = []
    for id in ids:
        for range in ranges:
            start, end = range.split("-")
            if int(start) <= id <= int(end):
                fresh_ids.append(id)
                break
    return len(fresh_ids)


def part2(lines):
    pass


if __name__ == "__main__":
    lines = read_lines(5)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
