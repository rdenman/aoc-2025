#!/usr/bin/env python3

import importlib
import sys

from aoc.utils import read_lines


def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py <day>")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
    except ValueError:
        print("Day must be a number (e.g., 1, 01, 10)")
        sys.exit(1)

    day_str = f"{day:02d}"

    module_name = f"aoc.day{day_str}.solution"
    try:
        solution = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Could not find module: {module_name}")
        print(f"Expected: aoc/day{day_str}/solution.py")
        sys.exit(1)

    try:
        lines = read_lines(day)
    except FileNotFoundError:
        print(f"Input not found: aoc/day{day_str}/input.txt")
        sys.exit(1)

    print(f"=== Advent of Code — Day {day_str} ===")

    if hasattr(solution, "part1"):
        try:
            print("Part 1:", solution.part1(lines))
        except Exception as e:
            print("Error running part1:", e)
    else:
        print("part1() not implemented")

    if hasattr(solution, "part2"):
        try:
            print("Part 2:", solution.part2(lines))
        except Exception as e:
            print("Error running part2:", e)
    else:
        print("part2() not implemented")


if __name__ == "__main__":
    main()
