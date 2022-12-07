from aocd import get_data
from ..utils.aoctimer import aoctimer
from typing import Self, TypedDict


class Directory(TypedDict):
    size: int
    parent: Self
    path: str


def parse_input(data: str) -> dict[str:Directory]:
    lines = data.splitlines()
    directories = {"/": {"size": 0, "path": "/", "parent": None}}
    pwd = directories["/"]
    for i in range(1, len(lines)):
        if lines[i].startswith("$ cd"):
            directory = lines[i][5:]
            pwd = (
                pwd["parent"]
                if directory == ".."
                else directories[f"{pwd['path']}{directory}/"]
            )
        elif lines[i].startswith("$ ls"):
            for line in lines[i + 1 :]:
                if line.startswith("$"):
                    break
                if line.startswith("dir"):
                    directory = line[4:]
                    if directory not in directories.keys():
                        directories[f"{pwd['path']}{directory}/"] = {
                            "size": 0,
                            "parent": pwd,
                            "path": f"{pwd['path']}{directory}/",
                        }
                else:
                    parent = pwd["parent"]
                    size = line.split(" ")[0]
                    pwd["size"] += int(size)
                    while parent:
                        parent["size"] += int(size)
                        parent = parent["parent"]
    return directories


@aoctimer
def part_a(data):
    return sum(
        directory["size"]
        for directory in parse_input(data).values()
        if directory["size"] < 100000
    )


@aoctimer
def part_b(data):
    directories = parse_input(data)
    needed_space = directories["/"]["size"] - 40000000
    directory_sizes = [directory["size"] for directory in directories.values()]
    directory_sizes.sort()
    for size in directory_sizes:
        if size > needed_space:
            return size


test_data = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

if __name__ == "__main__":
    assert part_a(test_data) == 95437
    assert part_b(test_data) == 24933642

    data = get_data(day=7, year=2022)
    print(part_a(data))
    print(part_b(data))
