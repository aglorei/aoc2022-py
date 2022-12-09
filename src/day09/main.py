from aocd import get_data
from ..utils.aoctimer import aoctimer


def parse_input(data: str) -> str:
    return [movement.split(" ") for movement in data.splitlines()]


def sign(x: int) -> int:
    return x and (1, -1)[x < 0]


compass = {"U": [0, 1], "R": [1, 0], "D": [0, -1], "L": [-1, 0]}


def articulate_tail(head: list[int], tail: list[int]) -> list[int]:
    follow_vector = [c1 - c2 for c1, c2 in zip(head, tail)]
    follow_vector_abs = [abs(coordinate) for coordinate in follow_vector]

    if sum(follow_vector_abs) == 3:
        long_idx = follow_vector_abs.index(2)
        follow_vector[1 - long_idx] += sign(follow_vector[1 - long_idx])

    return [c2 - sign(c2) + c1 for c1, c2 in zip(tail, follow_vector)]


def tail_positions_count(
    head: list[int], tails: list[list[int]], movements: list[str]
) -> int:
    tail_positions = set(["0,0"])

    for direction, steps in movements:
        steps = int(steps)
        while steps:
            head = [c1 + c2 for c1, c2 in zip(head, compass[direction])]
            steps -= 1

            next_knot = head
            for i in range(len(tails)):
                tails[i] = articulate_tail(next_knot, tails[i])
                next_knot = tails[i]

            tail_positions.add(",".join(map(str, tails[-1])))
    return len(tail_positions)


@aoctimer
def part_a(data: str) -> int:
    return tail_positions_count([0, 0], [[0, 0]], parse_input(data))


@aoctimer
def part_b(data: str) -> int:
    return tail_positions_count([0, 0], [[0, 0] for _ in range(9)], parse_input(data))


test_data_short = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

test_data_long = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

if __name__ == "__main__":
    assert part_a(test_data_short) == 13
    assert part_b(test_data_short) == 1
    assert part_b(test_data_long) == 36

    data = get_data(day=9, year=2022)
    print(part_a(data))
    print(part_b(data))
