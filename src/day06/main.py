from aocd import get_data
from ..utils.aoctimer import aoctimer


def characters_processed(data: str, window_size: int) -> int:
    for i in range(window_size - 1, len(data)):
        sequence = data[i - window_size + 1 : i + 1]
        if len(set(sequence)) == len(sequence):
            return i + 1


@aoctimer
def part_a(data):
    return characters_processed(data, 4)


@aoctimer
def part_b(data):
    return characters_processed(data, 14)


test_data_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test_data_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_data_3 = "nppdvjthqldpwncqszvftbrmjlhg"
test_data_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_data_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

if __name__ == "__main__":
    assert part_a(test_data_1) == 7
    assert part_a(test_data_2) == 5
    assert part_a(test_data_3) == 6
    assert part_a(test_data_4) == 10
    assert part_a(test_data_5) == 11
    assert part_b(test_data_1) == 19
    assert part_b(test_data_2) == 23
    assert part_b(test_data_3) == 23
    assert part_b(test_data_4) == 29
    assert part_b(test_data_5) == 26

    data = get_data(day=6, year=2022)
    print(part_a(data))
    print(part_b(data))
