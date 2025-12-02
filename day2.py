import re
import bisect

import file_handle


def parse_input(data: str) -> list[tuple[int, int]]:
    ranges = [tuple(map(int, row.split('-')))
              for row in data.split(',')]
    return ranges


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    ranges = parse_input(data)

    sum_invalid_ids = 0
    for (start, end) in ranges:
        for n in range(start, end+1):
            if re.fullmatch(r'(\d+)\1', str(n)):
                sum_invalid_ids += n

    return sum_invalid_ids


def part2_slow(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    ranges = parse_input(data)

    sum_invalid_ids = 0
    for (start, end) in ranges:
        for n in range(start, end+1):
            if re.fullmatch(r'(\d+)\1+', str(n)):
                sum_invalid_ids += n

    return sum_invalid_ids


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    ranges = parse_input(data)

    invalid_ids = set()
    max_end = max(end for _, end in ranges)
    mid = (len(str(max_end))+1) // 2
    half = str(max_end)[:mid]
    for n in range(1, int(half)+1):
        invalid_id = str(n)*2
        while int(invalid_id) <= max_end:
            invalid_ids.add(int(invalid_id))
            invalid_id += str(n)

    invalid_ids = sorted(list(invalid_ids))
    sum_invalid_ids = 0
    for (start, end) in ranges:
        left = bisect.bisect_right(invalid_ids, start)
        right = bisect.bisect_left(invalid_ids, end)
        sum_invalid_ids += sum(invalid_ids[left:right])

    return sum_invalid_ids


if __name__ == '__main__':
    print('Day #2, part one:', part1('./input/day2.txt'))
    print('Day #2, part two:', part2('./input/day2.txt'))
