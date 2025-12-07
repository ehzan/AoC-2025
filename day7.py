import file_handle
from collections import defaultdict


def parse_input(data: str) -> tuple[list[str], int]:
    grid = data.splitlines()
    start = grid[0].index('S')
    return grid, start


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid, start = parse_input(data)

    beams = {start}
    split_count = 0
    for row in grid[1:]:
        next_beams = set()
        for beam in beams:
            if row[beam] == '^':
                split_count += 1
                if 0 <= beam - 1:
                    next_beams.add(beam - 1)
                if beam + 1 < len(row):
                    next_beams.add(beam + 1)
            else:
                next_beams.add(beam)
        beams = next_beams

    return split_count


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    grid, start = parse_input(data)

    beam_counts = {start: 1}
    for row in grid[1:]:
        next_beam_counts = defaultdict(int)
        for beam, cnt in beam_counts.items():
            if row[beam] == '^':
                if 0 <= beam - 1:
                    next_beam_counts[beam - 1] += cnt
                if beam + 1 < len(row):
                    next_beam_counts[beam + 1] += cnt
            else:
                next_beam_counts[beam] += cnt
        beam_counts = next_beam_counts

    return sum(beam_counts.values())


if __name__ == '__main__':
    print('Day #7, part one:', part1('./input/day7.txt'))
    print('Day #7, part two:', part2('./input/day7.txt'))
