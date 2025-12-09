import file_handle
import geometry
from itertools import combinations
from collections import namedtuple
import time


Point = namedtuple('Point', ['x', 'y'])


def parse_input(data: str) -> list[Point]:
    vertices = [Point(*map(int, line.split(',')))
                for line in data.strip().splitlines()]
    return vertices


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    polygon = parse_input(data)

    max_area = 0
    for p1, p2 in combinations(polygon, 2):
        area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
        max_area = max(max_area, area)

    return max_area


def rectangle_corners(min_x, max_x, min_y, max_y) -> list[Point]:
    return [Point(min_x, min_y), Point(max_x, min_y),
            Point(max_x, max_y), Point(min_x, max_y)]


def is_point_inside(point, polygon) -> bool:
    inside = False
    n = len(polygon)
    for i in range(n):
        p1, p2 = polygon[i], polygon[(i + 1) % n]
        if p1.x == p2.x and min(p1.y, p2.y) <= point.y <= max(p1.y, p2.y):
            if point.x == p1.x:
                return True  # Point is on a vertical edge
            elif point.x < p1.x:
                inside = not inside  # Ray crosses vertical edge

    return inside


def is_rectangle_inside(rect, polygon) -> bool:
    mid = Point((rect[0] + rect[1]) // 2, (rect[2] + rect[3]) // 2)
    if not is_point_inside(mid, polygon):
        return False

    inscribed_rect = [rect[0]+1, rect[1]-1, rect[2]+1, rect[3]-1]
    inscribed_rect_corners = rectangle_corners(*inscribed_rect)

    n = len(polygon)
    rect_segments = [(inscribed_rect_corners[i], inscribed_rect_corners[(i + 1) % 4])
                     for i in range(4)]
    poly_segments = [(polygon[i], polygon[(i + 1) % n])
                     for i in range(n)]

    for rseg in rect_segments:
        for pseg in poly_segments:
            if geometry.segments_intersect(rseg, pseg):
                return False

    return True


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    polygon = parse_input(data)  # vertices of a rectilinear polygon

    max_area = 0
    for p1, p2 in combinations(polygon, 2):
        rect = (min(p1.x, p2.x), max(p1.x, p2.x),
                min(p1.y, p2.y), max(p1.y, p2.y),)
        area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
        if area > max_area and is_rectangle_inside(rect, polygon):
            max_area = area

    return max_area


if __name__ == '__main__':
    print('Day #9, part one:', part1('./input/day9.txt'))
    timestamp = time.time()
    print('Day #9, part two:', part2('./input/day9.txt'),
          f"(runtime: {round(time.time()-timestamp, 2)}s)")
