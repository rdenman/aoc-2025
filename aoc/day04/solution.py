from aoc.utils import read_lines


def get_adjacent(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    adj = []
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0:
                continue
            if 0 <= x + r < rows and 0 <= y + c < cols:
                adj.append(matrix[x + r][y + c])
    return adj


def part1(lines):
    matrix = []
    for line in lines:
        row = list(line)
        matrix.append(row)

    sum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == "@":
                adj = get_adjacent(matrix, x, y)
                rolls = [r for r in adj if "@" == r]
                if len(rolls) < 4:
                    sum += 1
    return sum


def part2(lines):
    matrix = []
    for line in lines:
        row = list(line)
        matrix.append(row)

    sum = 0
    prev = None
    while prev != sum:
        prev = sum
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == "@":
                    adj = get_adjacent(matrix, x, y)
                    rolls = [r for r in adj if "@" == r]
                    if len(rolls) < 4:
                        matrix[x][y] = "."
                        sum += 1
    return sum


if __name__ == "__main__":
    lines = read_lines(4)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
