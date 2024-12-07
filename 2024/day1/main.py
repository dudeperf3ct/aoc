
from collections import Counter
from pathlib import Path
import numpy as np
import pytest

# Test case
TEST_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
EXPECTED_PART1 = 11
EXPECTED_PART2 = 31



def read_input_file(file_path: Path =Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data

def problem_1(contents):
    data = []
    for c in contents.splitlines():
        data.extend(c.split("   "))
    left, right = np.sort(np.array(data[::2]).astype(int)), np.sort(np.array(data[1::2]).astype(int))
    return np.absolute(left-right).sum()

def problem_2(contents):
    data = []
    for c in contents.splitlines():
        data.extend(c.split("   "))
    left, right = np.array(data[::2]).astype(int), np.array(data[1::2]).astype(int)
    count_dict = Counter(right)
    res = 0
    for num in left:
        res += num * count_dict[num]
    return res



@pytest.mark.parametrize(
    ('test_input', 'expected'),
    (
        (TEST_INPUT, EXPECTED_PART1),
    ),
)
def test_part1(test_input: str, expected: int) -> None:
    assert problem_1(test_input) == expected



@pytest.mark.parametrize(
    ('test_input', 'expected'),
    (
        (TEST_INPUT, EXPECTED_PART2),
    ),
)
def test_part2(test_input: str, expected: int) -> None:
    assert problem_2(test_input) == expected



if __name__ == '__main__':

    contents = read_input_file("input")

    answer = problem_1(contents)
    print(answer)

    answer = problem_2(contents)
    print(answer)