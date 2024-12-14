from pathlib import Path

import pytest

from utils import WalkGrid

TEST_INPUT1 = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

EXPECTED_PART1 = 41


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


def problem_1(contents: str) -> int:
    data = contents.splitlines()
    g = WalkGrid(data)
    g.walk_grid()
    return g.count_distinct_place()


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT1, EXPECTED_PART1),),
)
def test_part1(test_input: str, expected: int) -> None:
    res = problem_1(test_input)
    assert res == expected


if __name__ == "__main__":
    contents = read_input_file("input")

    answer = problem_1(contents)
    print(answer)
