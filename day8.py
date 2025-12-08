import file_handle
import math
from collections import namedtuple, defaultdict


Point = namedtuple('Point', ['x', 'y', 'z'])


def distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


def parse_input(data: str) -> tuple[list[Point], list[tuple]]:
    vertices = [Point(*map(int, line.split(',')))
                for line in data.strip().splitlines()]
    edges = [(u, v, distance(vertices[u], vertices[v]),)
             for u in range(len(vertices))
             for v in range(u + 1, len(vertices))]
    edges.sort(key=lambda e: e[2])

    return vertices, edges


def kruskal(vertices: list[Point], edges: list[tuple]) -> tuple[list[tuple], set[frozenset]]:
    MST = []
    cluster = {v: {v} for v in range(len(vertices))}

    for (u, v, dist) in edges:
        if cluster[u] is not cluster[v]:
            MST.append((u, v))
            cluster[u].update(cluster[v])
            for node in cluster[v]:
                cluster[node] = cluster[u]
            if len(cluster[u]) == len(vertices):
                break

    clusters = set(map(frozenset, cluster.values()))
    return MST, clusters


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    vertices, edges = parse_input(data)

    _, circuits = kruskal(vertices, edges[:1000])
    three_largest_sizes = sorted(map(len, circuits), reverse=True)[:3]

    return math.prod(three_largest_sizes)


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    vertices, edges = parse_input(data)

    MST, _ = kruskal(vertices, edges)
    (u, v) = MST[-1]

    return vertices[u].x * vertices[v].x


if __name__ == '__main__':
    print('Day #8, part one:', part1('./input/day8.txt'))
    print('Day #8, part two:', part2('./input/day8.txt'))
