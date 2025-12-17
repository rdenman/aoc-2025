from aoc.day09.solution import part1, part2

EXAMPLE = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def test_part1():
    assert part1(EXAMPLE.splitlines()) == 50


def test_part2():
    assert part2(EXAMPLE.splitlines()) == None
