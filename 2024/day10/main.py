from pathlib import Path

import pytest

from utils import traverse_trail, traverse_trail1

TEST_INPUT11 = """\
0123
1234
8765
9876
"""

EXPECTED_PART11 = 1

TEST_INPUT12 = """\
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
"""

EXPECTED_PART12 = 2

TEST_INPUT13 = """\
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
"""

EXPECTED_PART13 = 4

TEST_INPUT14 = """\
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
"""

EXPECTED_PART14 = 3


TEST_INPUT15 = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

EXPECTED_PART15 = 36


TEST_INPUT21 = """\
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
"""

EXPECTED_PART21 = 3


TEST_INPUT22 = """\
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
"""

EXPECTED_PART22 = 13

TEST_INPUT23 = """\
012345
123456
234567
345678
4.6789
56789.
"""

EXPECTED_PART23 = 227

TEST_INPUT23 = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

EXPECTED_PART23 = 81


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


def problem_1(contents: str) -> int:
    data = []
    data = contents.splitlines()
    return traverse_trail(data)


def problem_2(contents: str) -> int:
    data = []
    data = contents.splitlines()
    return traverse_trail1(data)


@pytest.mark.parametrize(
    ("test_input", "expected"),
    (
        (TEST_INPUT11, EXPECTED_PART11),
        (TEST_INPUT12, EXPECTED_PART12),
        (TEST_INPUT13, EXPECTED_PART13),
        (TEST_INPUT14, EXPECTED_PART14),
        (TEST_INPUT15, EXPECTED_PART15),
    ),
)
def test_part1(test_input: str, expected: int) -> None:
    res = problem_1(test_input)
    assert res == expected


@pytest.mark.parametrize(
    ("test_input", "expected"),
    (
        (TEST_INPUT21, EXPECTED_PART21),
        (TEST_INPUT22, EXPECTED_PART22),
        (TEST_INPUT23, EXPECTED_PART23),
    ),
)
def test_part2(test_input: str, expected: int) -> None:
    res = problem_2(test_input)
    assert res == expected


if __name__ == "__main__":
    contents = read_input_file("input")

    answer = problem_1(contents)
    print(answer)

    answer = problem_2(contents)
    print(answer)
