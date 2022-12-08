from aocd import get_data
from ..utils.aoctimer import aoctimer
import math


def parse_input(data: str) -> list[list[int]]:
    return [[int(tree) for tree in row] for row in data.splitlines()]


def clear_view_count(trees: list[int], candidate: int) -> int:
    count = 0
    for tree in trees:
        count += 1
        if tree >= candidate:
            break
    return count


@aoctimer
def part_a(data: str) -> int:
    grid = parse_input(data)
    visible_count = len(grid) * 2 + len(grid[0]) * 2 - 4
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            candidate = grid[y][x]
            if (
                # east edge visibility
                max(grid[y][x + 1 :]) < candidate
                # west edge visibility
                or max(grid[y][:x]) < candidate
                # south edge visibility
                or max(map(lambda row: row[x], grid[y + 1 :])) < candidate
                # north edge visibility
                or max(map(lambda row: row[x], grid[:y])) < candidate
            ):
                visible_count += 1
    return visible_count


@aoctimer
def part_b(data: str) -> int:
    grid = parse_input(data)
    max_score = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            candidate = grid[y][x]
            score = math.prod(
                map(
                    lambda trees: clear_view_count(trees, candidate),
                    [
                        # east edge visibility
                        grid[y][x + 1 :],
                        # west edge visibility
                        grid[y][x - 1 :: -1],
                        # south edge visibility
                        map(lambda row: row[x], grid[y + 1 :]),
                        # north edge visibility
                        map(lambda row: row[x], grid[y - 1 :: -1]),
                    ],
                )
            )
            if score > max_score:
                max_score = score
    return max_score


test_data = """\
30373
25512
65332
33549
35390
"""

if __name__ == "__main__":
    assert part_a(test_data) == 21
    assert part_b(test_data) == 8

    data = get_data(day=8, year=2022)
    print(part_a(data))
    print(part_b(data))
