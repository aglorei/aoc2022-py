from aocd import get_data
from ..utils.aoctimer import aoctimer


def parse_input(data):
    return [map(letter_to_tuple, game[::2]) for game in data.splitlines()]


def letter_to_tuple(letter):
    return ord(letter) - ord('X' if letter in 'XYZ' else 'A') + 1


def play_rps(opponent, player):
    if (opponent % 3) + 1 == player:
        return player + 6
    elif opponent == player:
        return player + 3
    else:
        return player


@aoctimer
def part_a(data):
    return sum(play_rps(*game) for game in parse_input(data))


@aoctimer
def part_b(data):
    score = 0
    for opponent, outcome in parse_input(data):
        player = (outcome + opponent) % 3 + 1
        outcome = (outcome - 1) * 3
        score += player + outcome
    return score
    # Alternate solution to reuse the play_rps engine
    # return sum(play_rps(opponent, (outcome + opponent) % 3 + 1)
    #            for opponent, outcome in parse_input(data))


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
