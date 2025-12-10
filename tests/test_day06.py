from aoc.day06.solution import part1, part2

EXAMPLE = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_part1():
    assert part1(EXAMPLE.splitlines()) == 4277556


def test_part2():
    assert part2(EXAMPLE.splitlines()) == 3263827
