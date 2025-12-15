from itertools import combinations
import math
from aoc.utils import read_lines


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            # already connected
            return False

        # merge smaller into larger
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        self.count -= 1
        return True

    def component_sizes(self):
        comps = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            comps[root] = comps.get(root, 0) + 1
        return list(comps.values())


def distance(a: tuple[int, int, int], b: tuple[int, int, int]):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)


def part1(lines, n=1000):
    boxes = [tuple(map(int, line.split(","))) for line in lines]

    edges = []
    for i, j in combinations(range(len(boxes)), 2):
        edges.append((distance(boxes[i], boxes[j]), i, j))

    edges.sort()

    uf = UnionFind(len(boxes))
    for d, i, j in edges[:n]:
        uf.union(i, j)

    sizes = sorted(uf.component_sizes(), reverse=True)
    result = sizes[0] * sizes[1] * sizes[2]
    return result


def part2(lines):
    boxes = [tuple(map(int, line.split(","))) for line in lines]

    edges = []
    for i, j in combinations(range(len(boxes)), 2):
        edges.append((distance(boxes[i], boxes[j]), i, j))

    edges.sort()

    uf = UnionFind(len(boxes))
    last_edge = None

    for d, i, j in edges:
        if uf.union(i, j):
            last_edge = (boxes[i], boxes[j])
            if uf.count == 1:
                break

    return last_edge[0][0] * last_edge[1][0]


if __name__ == "__main__":
    lines = read_lines(-1)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
