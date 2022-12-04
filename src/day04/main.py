from aocd import get_data
from ..utils.aoctimer import aoctimer


def parse_input(data: str) -> list[set[int]]:
    assignments = [pairs.split(",") for pairs in data.splitlines()]
    result = []
    for pair in assignments:
        pair = [[int(seat) for seat in assignment.split("-")] for assignment in pair]
        pair = [set(range(assignment[0], assignment[1] + 1)) for assignment in pair]
        result.append(pair)
    return result


@aoctimer
def part_a(data):
    return sum(
        int(pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]))
        for pair in parse_input(data)
    )


@aoctimer
def part_b(data):
    return sum(int(not pair[0].isdisjoint(pair[1])) for pair in parse_input(data))


test_data = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

if __name__ == "__main__":
    assert part_a(test_data) == 2
    assert part_b(test_data) == 4

    data = get_data(day=4, year=2022)
    print(part_a(data))
    print(part_b(data))
