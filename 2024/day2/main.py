from pathlib import Path

import pytest

TEST_INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

EXPECTED_PART1 = 2

EXPECTED_PART2 = 4


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


def analyse_level_saftey(level):
    inc, dec = 0, 0
    for i in range(len(level) - 1):
        if level[i] >= level[i + 1]:
            inc += 1
        else:
            dec += 1
    if not (inc == len(level) - 1 or dec == len(level) - 1):
        return False
    for i in range(len(level) - 1):
        diff = abs(level[i] - level[i + 1])
        if not (1 <= diff and diff <= 3):
            return False
    return True


def problem_1(contents: str) -> int:
    reports, result = [], []
    for c in contents.splitlines():
        lines = c.split(" ")
        reports.append([int(val) for val in lines])
    for level in reports:
        result.append(analyse_level_saftey(level))
    return sum(result)


def problem_2(contents: str) -> int:
    reports, result = [], []
    for c in contents.splitlines():
        lines = c.split(" ")
        reports.append([int(val) for val in lines])
    for level in reports:
        res = analyse_level_saftey(level)
        if not res:
            for i in range(len(level)):
                new_level = level[:i] + level[i + 1 :]
                res = analyse_level_saftey(new_level)
                if res:
                    break
        result.append(res)
    return sum(result)


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT, EXPECTED_PART1),),
)
def test_part1(test_input: str, expected: int) -> None:
    res = problem_1(test_input)
    assert res == expected


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT, EXPECTED_PART2),),
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
