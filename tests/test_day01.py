from aoc.day01.solution import part1, part2

EXAMPLE = """\
199
200
208
210
"""


def test_part1():
    assert part1(EXAMPLE.splitlines()) == 7


def test_part2():
    assert part2(EXAMPLE.splitlines()) == 5
