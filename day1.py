import file_handle


def parse_input(data: str) -> list[tuple[str, int]]:
    rotations = [(line[0], int(line[1:])) for line in data.splitlines()]
    return rotations


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rotations = parse_input(data)

    pos = 50
    zero_count = 0
    for (direction, distance) in rotations:
        pos += (distance if direction == 'R' else -distance)
        pos %= 100
        zero_count += (pos == 0)

    return zero_count


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rotations = parse_input(data)

    pos = 50
    zero_count = 0
    for (direction, distance) in rotations:
        pre = pos
        zero_count += distance // 100
        distance %= 100
        pos += (distance if direction == 'R' else -distance)
        zero_count += (pre != 0 and not 0 < pos < 100)
        pos %= 100

    return zero_count


if __name__ == '__main__':
    print('Day #1, part one:', part1('./input/day1.txt'))
    print('Day #1, part two:', part2('./input/day1.txt'))
