from aoc.day03.solution import part1, part2

EXAMPLE = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_part1():
    assert part1(EXAMPLE.splitlines()) == 357


def test_part2():
    assert part2(EXAMPLE.splitlines()) == 3121910778619
