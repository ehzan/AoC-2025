import re
import file_handle
import pulp


class Machine:
    def __init__(self, desc: str):
        self.lights = re.search(r'\[(.*?)\]', desc).group(1)

        buttons_match = re.findall(r'\((.*?)\)', desc)
        self.buttons = [set(map(int, buttons_str.split(',')))
                        for buttons_str in buttons_match]

        joltages_match = re.search(r'\{(.*?)\}', desc)
        self.joltages = tuple(map(int, joltages_match.group(1).split(',')))


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    machines = [Machine(desc=line) for line in data.splitlines()]

    total_presses = 0
    for machine in machines:
        m, n = len(machine.lights), len(machine.buttons)
        # linear programming problem:
        problem = pulp.LpProblem(name="lights", sense=pulp.LpMinimize)
        # variables:
        x = [pulp.LpVariable(name=f'x{i}', cat='Binary')
             for i in range(n)]
        # helper variables for parity:
        k = [pulp.LpVariable(f"k{j}", lowBound=0, cat="Integer")
             for j in range(m)]
        # constraints:
        for j in range(m):
            toggle_count_j = pulp.lpSum(x[i]
                                        for i in range(n) if j in machine.buttons[i])
            problem += toggle_count_j == 2*k[j] + int(machine.lights[j] == '#')
        # objective:
        problem += pulp.lpSum(x)

        problem.solve(pulp.PULP_CBC_CMD(msg=False))
        total_presses += int(pulp.value(problem.objective))

    return total_presses


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    machines = [Machine(desc=line) for line in data.splitlines()]

    total_presses = 0
    for machine in machines:
        n = len(machine.buttons)
        # linear programming problem:
        problem = pulp.LpProblem(name="joltages", sense=pulp.LpMinimize)
        # variables:
        x = [pulp.LpVariable(name=f'x{i}', lowBound=0, cat='Integer')
             for i in range(n)]
        # constraints:
        for j in range(len(machine.joltages)):
            joltage_j = pulp.lpSum(x[i]
                                   for i in range(n) if j in machine.buttons[i])
            problem += joltage_j == machine.joltages[j]
        # objective:
        problem += pulp.lpSum(x)

        problem.solve(pulp.PULP_CBC_CMD(msg=False))
        total_presses += int(pulp.value(problem.objective))

    return total_presses


if __name__ == '__main__':
    print('Day #10, part one:', part1('./input/day10.txt'))
    print('Day #10, part two:', part2('./input/day10.txt'))
