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
    strRanges = parse_input(lines)[0]
    ranges = []
    for r in strRanges:
        start, end = r.split("-")
        ranges.append([int(start), int(end)])

    ranges = sorted(ranges, key=lambda x: x[0])

    merged = []
    for start, end in ranges:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    sum = 0
    for start, end in merged:
        sum += end - start + 1
    return sum


if __name__ == "__main__":
    lines = read_lines(5)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
