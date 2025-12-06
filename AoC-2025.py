import timeit

answers = {'day1': (1023, 5899),
           'day2': (44854383294, 55647141923),
           'day3': (16973, 168027167146027),
           'day4': (1480, 8899),
           'day5': (577, 350513176552950),
           'day6': (6757749566978, 10603075273949),
           'day7': (0, 0),
           'day8': (0, 0),
           'day9': (0, 0),
           'day10': (0, 0),
           'day11': (0, 0),
           'day12': (0, 0),
           }

if __name__ == '__main__':
    for i in range(1, 13):
        if answers[f'day{i}'] == (0, 0):
            continue
        t = timeit.timeit(stmt=f"ans = day{i}.part1('./input/day{i}.txt');" +
                          f"print('Day #{i}, part one:', ans, end='  \t', );" +
                          f"assert ans == answers['day{i}'][0];",
                          setup=f"import day{i}",
                          globals={'answers': answers},
                          number=1)
        print(f"{'✅' if t < 5 else '⚠️ '}(runtime: {round(t, 2)}s)")

        if i == 12:
            break

        t = timeit.timeit(stmt=f"ans = day{i}.part2('./input/day{i}.txt');" +
                          f"print('Day #{i}, part two:', ans, end='  \t', );" +
                          f"assert ans == answers['day{i}'][1];",
                          setup=f"import day{i}",
                          globals={'answers': answers},
                          number=1)
        print(f"{'✅' if t < 5 else '⚠️ '}(runtime: {round(t, 2)}s)")
        print()
