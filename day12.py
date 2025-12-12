import file_handle


def parse_input(data: str) -> tuple[list[str], list[int], list[tuple[int, int]], list[list[int]]]:
    sections = data.split('\n\n')
    shape_blocks = sections[:-1]
    region_lines = sections[-1].splitlines()

    shapes = [block.partition('\n')[2] for block in shape_blocks]
    shape_sizes = [shape.count('#') for shape in shapes]

    regions = []
    shape_counts_list = []
    for line in region_lines:
        dims_str, counts_str = line.split(': ')
        regions.append(tuple(map(int, dims_str.split('x'))))
        shape_counts_list.append(list(map(int, counts_str.split())))

    return shapes, shape_sizes, regions, shape_counts_list


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    shapes, shape_sizes, regions, shape_counts_list = parse_input(data)

    feasible_count = 0
    for (w, h), shape_counts in zip(regions, shape_counts_list):
        area_demand = sum(count * size
                          for count, size in zip(shape_counts, shape_sizes))
        tiles_3x3 = (w // 3) * (h // 3)

        necessary_condition = area_demand <= w * h
        sufficient_condition = sum(shape_counts) <= tiles_3x3
        assert necessary_condition == sufficient_condition, (
            f"region: {w}x{h}, shape counts: {shape_counts}")

        feasible_count += necessary_condition

    return feasible_count


if __name__ == '__main__':
    print('Day #12, part one:', part1('./input/day12.txt'))
