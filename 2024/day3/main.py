import re
from pathlib import Path

import pytest

TEST_INPUT1 = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

TEST_INPUT2 = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

EXPECTED_PART1 = 161

EXPECTED_PART2 = 48


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


def problem_1(contents: str) -> int:
    candidates = re.findall(pattern=r"mul\(\d{1,3}\,\d{1,3}\)", string=contents)
    res = 0
    for cand in candidates:
        numbers = re.findall(pattern=r"\d{1,3}", string=cand)
        res += int(numbers[0]) * int(numbers[1])
    return res


def problem_2(contents: str) -> int:
    matches = re.findall(
        pattern=r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", string=contents
    )

    include = True
    res = 0
    for match_string in matches:
        if match_string == "do()":
            include = True
        elif match_string == "don't()":
            include = False
        else:
            if include:
                numbers = re.findall(pattern=r"\d{1,3}", string=match_string)
                res += int(numbers[0]) * int(numbers[1])
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
    ((TEST_INPUT2, EXPECTED_PART2),),
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
