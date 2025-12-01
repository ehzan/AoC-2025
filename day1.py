import file_handle


def parse_input(data: str) -> list[tuple[str, int]]:
    rotations = [(row[0], int(row[1:])) for row in data.splitlines()]
    return rotations


def puzzle1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rotations = parse_input(data)

    pos = 50
    zero_count = 0
    for d, l in rotations:
        pos += l * (1 if d == 'R' else -1)
        pos %= 100
        zero_count += pos == 0

    return zero_count


def puzzle2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    rotations = parse_input(data)

    pos = 50
    zero_count = 0
    for d, l in rotations:
        pre = pos
        zero_count += l//100
        l %= 100
        pos += l * (1 if d == 'R' else -1)
        zero_count += (pre != 0 and not 0 < pos < 100)
        pos %= 100

    return zero_count


if __name__ == '__main__':
    print('Day #1, part one:', puzzle1('./input/day1.txt'))
    print('Day #1, part two:', puzzle2('./input/day1.txt'))
