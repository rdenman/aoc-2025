from aoc.day05.solution import part1, part2

EXAMPLE = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_part1():
    assert part1(EXAMPLE.splitlines()) == 3


def test_part2():
    assert part2(EXAMPLE.splitlines()) == None
