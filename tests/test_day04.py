from aoc.day04.solution import part1, part2

EXAMPLE = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_part1():
    assert part1(EXAMPLE.splitlines()) == 13


def test_part2():
    assert part2(EXAMPLE.splitlines()) == 43
