import re
import bisect

import file_handle


def parse_input(data: str) -> list[tuple[int, int]]:
    ranges = [tuple(map(int, row.split('-')))
              for row in data.split(',')]
    return ranges


def puzzle1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    ranges = parse_input(data)

    sum_invalid_ids = 0
    for start, end in ranges:
        for n in range(start, end+1):
            if re.fullmatch(r'(\d+)\1', str(n)):
                sum_invalid_ids += n

    return sum_invalid_ids


def puzzle2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    ranges = parse_input(data)

    sum_invalid_ids = 0
    for start, end in ranges:
        for n in range(start, end+1):
            if re.fullmatch(r'(\d+)\1+', str(n)):
                sum_invalid_ids += n

    return sum_invalid_ids


if __name__ == '__main__':
    print('Day #2, part one:', puzzle1('./input/day2.txt'))
    print('Day #2, part two:', puzzle2('./input/day2.txt'))
