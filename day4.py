import file_handle


def count_adjacents(grid: list, x: int, y: int) -> int:
    max_x, max_y = len(grid[0]), len(grid)
    return sum(0 <= x+dx < max_x and 0 <= y+dy < max_y and
               (dx, dy) != (0, 0) and grid[y+dy][x+dx] == '@'
               for dx in [-1, 0, 1] for dy in [-1, 0, 1])


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = data.splitlines()

    accessible_count = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            accessible_count += grid[y][x] == '@' and count_adjacents(
                grid, x, y) < 4

    return accessible_count


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid = [list(row) for row in data.splitlines()]

    total_removed = 0
    accessible = {1}
    while accessible:
        accessible.clear()
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == '@' and count_adjacents(grid, x, y) < 4:
                    accessible.add((x, y))

        for x, y in accessible:
            grid[y][x] = '.'
        total_removed += len(accessible)

    return total_removed


if __name__ == '__main__':
    print('Day #4, part one:', part1('./input/day4.txt'))
    print('Day #4, part two:', part2('./input/day4.txt'))
