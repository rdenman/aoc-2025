from aoc.utils import read_lines


def part1(lines):
    for idx, cell in enumerate(lines[0]):
        if cell == "S":
            start = idx
            break

    beams = [(0, start)]
    count = 0

    rows = len(lines)
    cols = len(lines[0])
    visited = set()

    while beams:
        r, c = beams.pop()
        if (r, c) in visited or r >= rows:
            continue
        visited.add((r, c))

        if lines[r][c] == "^":
            count += 1
            if c - 1 >= 0:
                beams.append((r + 1, c - 1))
            if c + 1 < cols:
                beams.append((r + 1, c + 1))
        else:
            beams.append((r + 1, c))

    return count


def part2(lines):
    pass


if __name__ == "__main__":
    lines = read_lines(-1)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
