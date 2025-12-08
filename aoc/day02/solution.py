from aoc.utils import read_lines
import re


def part1(lines):
    sum = 0
    ranges = lines[0].split(",")
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            s = str(i)
            if len(s) % 2 == 0:
                l = len(s)
                if s[0 : l // 2] == s[l // 2 :]:
                    sum += i
    return sum


def part2(lines):
    sum = 0
    ranges = lines[0].split(",")
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            s = str(i)
            for pattern_len in range(1, len(s) // 2 + 1):
                if len(s) % pattern_len == 0:
                    pattern = s[:pattern_len]
                    repeats = len(s) // pattern_len
                    if pattern * repeats == s:
                        sum += i
                        break
    return sum


if __name__ == "__main__":
    lines = read_lines(2)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
