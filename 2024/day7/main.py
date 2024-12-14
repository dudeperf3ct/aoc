from pathlib import Path

import pytest

from utils import eval_numbers

TEST_INPUT1 = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

EXPECTED_PART1 = 3749
EXPECTED_PART2 = 11387


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


def problem_1(contents: str) -> int:
    outputs, numbers = [], []
    for data in contents.splitlines():
        line = data.split(":")
        outputs.append(int(line[0].strip()))
        numbers.append([int(num) for num in line[1].strip().split(" ")])
    res = 0
    for out, nums in zip(outputs, numbers):
        res += eval_numbers(output=out, numbers=nums)
    return res


def problem_2(contents: str) -> int:
    outputs, numbers = [], []
    for data in contents.splitlines():
        line = data.split(":")
        outputs.append(int(line[0].strip()))
        numbers.append([int(num) for num in line[1].strip().split(" ")])
    res = 0
    for out, nums in zip(outputs, numbers):
        res += eval_numbers(output=out, numbers=nums, use_concat=True)
    return res


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT1, EXPECTED_PART1),),
)
def test_part1(test_input: str, expected: int) -> None:
    res = problem_1(test_input)
    assert res == expected


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT1, EXPECTED_PART2),),
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
