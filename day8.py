import file_handle
import math
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y', 'z'])


def parse_input(data: str) -> list[Point]:
    points = [Point(*map(int, line.split(','))) for line in data.splitlines()]
    return points


def distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


def generate_edges(points: list[Point]) -> list[tuple]:
    edges = []
    n = len(points)
    for u in range(n):
        for v in range(u + 1, n):
            edges.append(((u, v), distance(points[u], points[v]),))
    return sorted(edges, key=lambda e: e[1])


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    points = parse_input(data)

    circuits = {i: {i} for i in range(len(points))}
    edges = generate_edges(points)

    for ((u, v), dist) in edges[:1000]:
        if circuits[u] is not circuits[v]:
            circuits[u].update(circuits[v])
            for node in circuits[v]:
                circuits[node] = circuits[u]

    max_circuits = [set(), set(), set()]
    for circuit in circuits.values():
        if circuit not in max_circuits and len(circuit) > len(max_circuits[2]):
            max_circuits[2] = circuit
            if len(max_circuits[2]) > len(max_circuits[1]):
                max_circuits[1], max_circuits[2] = max_circuits[2], max_circuits[1]
                if len(max_circuits[1]) > len(max_circuits[0]):
                    max_circuits[0], max_circuits[1] = max_circuits[1], max_circuits[0]

    return math.prod(map(len, max_circuits))


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    points = parse_input(data)

    circuits = {i: {i} for i in range(len(points))}
    edges = generate_edges(points)

    for ((u, v), dist) in edges:
        if circuits[u] is not circuits[v]:
            circuits[u].update(circuits[v])
            for node in circuits[v]:
                circuits[node] = circuits[u]
            if len(circuits[u]) == len(points):
                last = (u, v)
                break

    return points[last[0]].x * points[last[1]].x


if __name__ == '__main__':
    print('Day #8, part one:', part1('./input/day8.txt'))
    print('Day #8, part two:', part2('./input/day8.txt'))
