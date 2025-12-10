from aoc.utils import read_lines


def op(operator, items):
    if operator == "*":
        val = 1
        for item in items:
            val *= int(item)
        return val
    elif operator == "+":
        val = 0
        for item in items:
            val += int(item)
        return val
    else:
        raise ValueError(f"Invalid operator: {operator}")


def part1(lines):
    items = []
    for line in lines:
        items.append(list(filter(lambda x: x != "", line.strip().split(" "))))
    sum = 0
    for i in range(len(items[0])):
        nums = []
        for arr in items:
            if arr[i] != "*" and arr[i] != "+":
                nums.append(arr[i])
        sum += op(items[-1][i], nums)
    return sum


def part2(lines):
    pass


if __name__ == "__main__":
    lines = read_lines(-1)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
