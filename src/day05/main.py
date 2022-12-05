from aocd import get_data
from ..utils.aoctimer import aoctimer
from typing import TypedDict


Move = TypedDict("Move", {"quantity": int, "to": int, "from": int})
ParsedInput = TypedDict("ParsedInput", {"crates": list[list[str]], "moves": list[Move]})


def parse_input(data: str) -> ParsedInput:
    data = data.splitlines()
    divider_idx = data.index("")

    crates = []
    for crate_number in data[divider_idx - 1].strip().split("   "):
        crate = []
        for idx in range(divider_idx - 2, -1, -1):
            letter = data[idx][int(crate_number) * 4 - 3]
            if letter.strip():
                crate.append(letter)
        crates.append(crate)

    moves = []
    for move in data[divider_idx + 1 :]:
        move = move.split(" ")
        moves.append(
            {"quantity": int(move[1]), "from": int(move[3]) - 1, "to": int(move[5]) - 1}
        )

    return {"crates": crates, "moves": moves}


@aoctimer
def part_a(data: str) -> str:
    parsed_data = parse_input(data)
    for move in parsed_data["moves"]:
        for _ in range(move["quantity"]):
            parsed_data["crates"][move["to"]].append(parsed_data["crates"][move["from"]].pop())
    return "".join([crate.pop() for crate in parsed_data["crates"]])


@aoctimer
def part_b(data: str) -> str:
    parsed_data = parse_input(data)
    for move in parsed_data["moves"]:
        buffer = []
        for _ in range(move["quantity"]):
            buffer.append(parsed_data["crates"][move["from"]].pop())
        for _ in range(move["quantity"]):
            parsed_data["crates"][move["to"]].append(buffer.pop())
    return "".join([crate.pop() for crate in parsed_data["crates"]])


test_data = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

if __name__ == "__main__":
    assert part_a(test_data) == "CMZ"
    assert part_b(test_data) == "MCD"

    data = get_data(day=5, year=2022)
    print(part_a(data))
    print(part_b(data))
