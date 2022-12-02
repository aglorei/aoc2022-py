from aocd import get_data
from ..utils.aoctimer import aoctimer


def parse_input(data):
    return data.splitlines()


def play_rps(opponent, player):
    opponent = ord(opponent) - ord("A") + 1
    player = ord(player) - ord("X") + 1
    if (opponent % 3) + 1 == player:
        return player + 6
    elif opponent == player:
        return player + 3
    else:
        return player


@aoctimer
def part_a(data):
    rounds = [(round[0], round[-1]) for round in parse_input(data)]
    return sum(play_rps(*round) for round in rounds)


@aoctimer
def part_b(data):
    rounds = []
    for round in parse_input(data):
        outcome = ord(round[-1]) - ord("X") - 1
        modifier = (ord(round[0]) - ord("A") + outcome) % 3
        player = chr(modifier + ord("X"))
        rounds.append((round[0], player))
    return sum(play_rps(*round) for round in rounds)


test_data = """\
A Y
B X
C Z
"""

if __name__ == "__main__":
    assert part_a(test_data) == 15
    assert part_b(test_data) == 12

    data = get_data(day=2, year=2022)
    print(part_a(data))
    print(part_b(data))
