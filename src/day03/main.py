from aocd import get_data
from ..utils.aoctimer import aoctimer


def parse_input(data: str) -> str:
    return data.splitlines()


def get_common_item(*rucksacks: list[list[str]]) -> str:
    rucksack_sets = [set(rucksack) for rucksack in rucksacks]
    return rucksack_sets[0].intersection(*rucksack_sets[1:]).pop()


def get_item_priority(item: str) -> int:
    modifier = 38 if item.isupper() else 96
    return ord(item) - modifier


@aoctimer
def part_a(data: str) -> int:
    priority_sum = 0
    for rucksack in parse_input(data):
        half = len(rucksack) // 2
        item = get_common_item(rucksack[:half], rucksack[half:])
        priority_sum += get_item_priority(item)
    return priority_sum


@aoctimer
def part_b(data: str) -> int:
    priority_sum = 0
    rucksacks = parse_input(data)
    for i in range(0, len(rucksacks), 3):
        item = get_common_item(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2])
        priority_sum += get_item_priority(item)
    return priority_sum


test_data = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

if __name__ == "__main__":
    assert part_a(test_data) == 157
    assert part_b(test_data) == 70

    data = get_data(day=3, year=2022)
    print(part_a(data))
    print(part_b(data))
