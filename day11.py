import file_handle
from functools import cache


def parse_input(data: str) -> dict[str, list[str]]:
    adjacency_list = {node: adjacent_nodes.split()
                      for (node, adjacent_nodes) in
                      (line.split(': ', 1) for line in data.splitlines())
                      }
    return adjacency_list


def count_paths(source: str, target: str, DAG: dict[str, list[str]]) -> int:

    @cache
    def dfs(node: str, target: str) -> int:
        if node == target:
            return 1
        if node not in DAG:
            return 0
        return sum(dfs(adj, target) for adj in DAG[node])

    return dfs(source, target)


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    DAG = parse_input(data)
    return count_paths('you', 'out', DAG)


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    DAG = parse_input(data)

    svr_dac_fft_out = count_paths(
        'svr', 'dac', DAG) * count_paths('dac', 'fft', DAG) * count_paths('fft', 'out', DAG)
    svr_fft_dac_out = count_paths(
        'svr', 'fft', DAG) * count_paths('fft', 'dac', DAG) * count_paths('dac', 'out', DAG)

    return svr_dac_fft_out + svr_fft_dac_out


if __name__ == '__main__':
    print('Day #11, part one:', part1('./input/day11.txt'))
    print('Day #11, part two:', part2('./input/day11.txt'))
