import file_handle


def parse_input(data: str) -> tuple[list[tuple], list[int]]:
    ranges_section, ids_section = data.split('\n\n')
    ranges = [tuple(map(int, line.split('-')))
              for line in ranges_section.splitlines()]
    ids = list(map(int, ids_section.splitlines()))
    return ranges, ids


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    ranges, ids = parse_input(data)
    return sum(any(start <= id <= end for (start, end) in ranges)
               for id in ids)


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    ranges, _ = parse_input(data)

    ranges.sort()
    merged = [ranges[0]]
    for (start, end) in ranges:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    return sum(end - start + 1 for start, end in merged)


if __name__ == '__main__':
    print('Day #5, part one:', part1('./input/day5.txt'))
    print('Day #5, part two:', part2('./input/day5.txt'))
