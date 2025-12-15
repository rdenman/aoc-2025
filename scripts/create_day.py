#!/usr/bin/env python3
"""
Script to create a new Advent of Code day folder with template files.
Usage: python create_day.py <day_number>
"""
import sys
from pathlib import Path


SOLUTION_TEMPLATE = """from aoc.utils import read_lines


def part1(lines):
    pass


def part2(lines):
    pass


if __name__ == "__main__":
    lines = read_lines(-1)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
"""

TEST_TEMPLATE = """from aoc.day{day:02d}.solution import part1, part2

EXAMPLE = \"\"\"\\

\"\"\"


def test_part1():
    assert part1(EXAMPLE.splitlines()) == None


def test_part2():
    assert part2(EXAMPLE.splitlines()) == None
"""


def create_day(day_number):
    """Create a new day folder with template files."""
    # Validate day number
    try:
        day = int(day_number)
        if day < 1 or day > 25:
            print("Error: Day number must be between 1 and 25")
            return False
    except ValueError:
        print("Error: Day number must be a valid integer")
        return False

    # Get the workspace root (script is in scripts/ subdirectory)
    workspace_root = Path(__file__).parent.parent

    # Create day folder
    day_folder = workspace_root / "aoc" / f"day{day:02d}"
    if day_folder.exists():
        print(f"Error: {day_folder} already exists")
        return False

    print(f"Creating {day_folder}...")
    day_folder.mkdir(parents=True, exist_ok=True)

    # Create solution.py
    solution_file = day_folder / "solution.py"
    solution_file.write_text(SOLUTION_TEMPLATE.lstrip())
    print(f"  Created {solution_file.name}")

    # Create empty input.txt
    input_file = day_folder / "input.txt"
    input_file.write_text("")
    print(f"  Created {input_file.name}")

    # Create empty problem.txt
    problem_file = day_folder / "problem.txt"
    problem_file.write_text("")
    print(f"  Created {problem_file.name}")

    # Create test file
    test_folder = workspace_root / "tests"
    test_file = test_folder / f"test_day{day:02d}.py"

    if test_file.exists():
        print(f"Warning: {test_file} already exists, skipping...")
    else:
        test_file.write_text(TEST_TEMPLATE.format(day=day).lstrip())
        print(f"Created {test_file}")

    print(f"\n✅ Day {day:02d} created successfully!")
    print(f"   - Solution: {day_folder}/solution.py")
    print(f"   - Test: {test_file}")
    return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python create_day.py <day_number>")
        print("Example: python create_day.py 9")
        sys.exit(1)

    day_number = sys.argv[1]
    success = create_day(day_number)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
