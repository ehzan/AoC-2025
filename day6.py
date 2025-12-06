import file_handle
import math
from itertools import zip_longest


def parse_input(data: str) -> tuple[list[list[str]], list[str]]:
    lines = data.splitlines()
    numbers_lists = [line.split() for line in lines[:-1]]
    numbers_lists = list(zip(*numbers_lists))
    operations = lines[-1].split()

    return numbers_lists, operations


def split_by_value(lst: list, value) -> list[list]:
    # Split a list into sublists by a separator value.
    result, current = [], []
    for item in lst:
        if item == value:
            result.append(current)
            current = []
        else:
            current.append(item)
    result.append(current)

    return result


def parse_input_rtl(data: str) -> tuple[list[list[str]], list[str]]:
    lines = data.splitlines()
    numbers = [''.join(digit) for digit in
               zip_longest(*lines[:-1], fillvalue=' ')]
    numbers_lists = split_by_value(numbers, ' '*(len(lines)-1))
    operations = lines[-1].split()

    return numbers_lists, operations


def do_math(numbers: list, op: str) -> int:
    match op:
        case '+':
            return sum(numbers)
        case '*':
            return math.prod(numbers)
        case _:
            raise ValueError(f"Unsupported operation: {op}")


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    numbers_lists, operations = parse_input(data)

    grand_total = 0
    for nums, op in zip(numbers_lists, operations):
        grand_total += do_math(map(int, nums), op)

    return grand_total


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    numbers_lists, operations = parse_input_rtl(data)

    grand_total = 0
    for nums, op in zip(numbers_lists, operations):
        grand_total += do_math(map(int, nums), op)

    return grand_total


if __name__ == '__main__':
    print('Day #6, part one:', part1('./input/day6.txt'))
    print('Day #6, part two:', part2('./input/day6.txt'))
