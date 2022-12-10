from aocd import get_data
from ..utils.aoctimer import aoctimer


def parse_input(data: str) -> list[list[int]]:
    return [[0] if line == "noop" else [int(line[4:]), 0] for line in data.splitlines()]


@aoctimer
def part_a(data: str) -> int:
    instructions = parse_input(data)

    cycle = 0
    register = 1
    signal_sum = 0

    for modifier_stack in instructions:
        while modifier_stack:
            cycle += 1

            if cycle % 40 == 20:
                signal_sum += cycle * register
                if cycle == 220:
                    return signal_sum

            register += modifier_stack.pop()


@aoctimer
def part_b(data: str) -> str:
    instructions = parse_input(data)

    cycle = 0
    register = 1

    display = [["." for _ in range(40)] for _ in range(6)]

    for modifier_stack in instructions:
        while modifier_stack:
            column = cycle % 40
            if abs(column - register) < 2:
                row = cycle // 40
                display[row][column] = "#"
            cycle += 1
            register += modifier_stack.pop()

    # TODO: Use OCR to parse lettering
    print_display = "\n".join([" ".join(line) for line in display])
    return print_display


test_data = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

if __name__ == "__main__":
    assert part_a(test_data) == 13140
    assert (
        part_b(test_data)
        == """\
# # . . # # . . # # . . # # . . # # . . # # . . # # . . # # . . # # . . # # . .
# # # . . . # # # . . . # # # . . . # # # . . . # # # . . . # # # . . . # # # .
# # # # . . . . # # # # . . . . # # # # . . . . # # # # . . . . # # # # . . . .
# # # # # . . . . . # # # # # . . . . . # # # # # . . . . . # # # # # . . . . .
# # # # # # . . . . . . # # # # # # . . . . . . # # # # # # . . . . . . # # # #
# # # # # # # . . . . . . . # # # # # # # . . . . . . . # # # # # # # . . . . ."""
    )

    data = get_data(day=10, year=2022)
    print(part_a(data))
    print(part_b(data))
