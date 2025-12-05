
import file_handle


def part1(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    banks = data.splitlines()

    total_joltage = 0
    for bank in banks:
        digit1 = max(bank[:-1])
        digit2 = max(bank[bank.index(digit1) + 1:])
        total_joltage += int(digit1 + digit2)

    return total_joltage


def part2(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    banks = data.splitlines()

    total_joltage = 0
    for bank in banks:
        if len(bank) > 12:
            joltage = ''
            for i in range(12):
                max_digit = max(bank[:len(bank) - (11 - i)])
                joltage += max_digit
                bank = bank[bank.index(max_digit) + 1:]
        else:
            joltage = bank
        total_joltage += int(joltage)

    return total_joltage


if __name__ == '__main__':
    print('Day #3, part one:', part1('./input/day3.txt'))
    print('Day #3, part two:', part2('./input/day3.txt'))
