from collections import defaultdict
from functools import cache
from pathlib import Path

import pytest

TEST_INPUT1 = """\
125 17
"""

EXPECTED_PART1 = 55312


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


@cache
def transform_element(d):
    if d == 0:
        return [1]
    elif len(str(d)) % 2 == 0:
        str_num = str(d)
        return [int(str_num[: len(str_num) // 2]), int(str_num[len(str_num) // 2 :])]
    else:
        return [d * 2024]


@cache
def blink_once(num, blink):
    if blink == 0:
        return 1
    return sum(blink_once(n, blink - 1) for n in transform_element(num))


def count_with_dict(data, blink):
    res = defaultdict(int)
    for num in data:
        res[num] += 1
    for _ in range(blink):
        res_new = defaultdict(int)
        for k in res.keys():
            if k == 0:
                res_new[1] += res[0]
            elif len(str(k)) % 2 == 0:
                str_num = str(k)
                res_new[int(str_num[: len(str_num) // 2])] += res[k]
                res_new[int(str_num[len(str_num) // 2 :])] += res[k]
            else:
                res_new[2024 * k] += res[k]
        res = res_new
    return sum(res.values())


def problem_1(contents: str) -> int:
    data = [int(n) for n in contents.split(" ")]
    # total = 0
    # for num in data:
    #     total += blink_once(num, 25)
    # return total
    return count_with_dict(data, 25)


def problem_2(contents: str) -> int:
    data = [int(n) for n in contents.split(" ")]
    total = 0
    for num in data:
        total += blink_once(num, 75)
    return total
    # return count_with_dict(data, 75)


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

    answer = problem_2(contents)
    print(answer)
