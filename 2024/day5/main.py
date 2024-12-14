from collections import defaultdict
from pathlib import Path

import pytest

TEST_INPUT1 = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

EXPECTED_PART1 = 143

EXPECTED_PART2 = 123


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


def is_valid_first(data, num, arr):
    for val in arr:
        if num in data[val]:
            return False
    return True


def is_valid_order(data, order) -> bool:
    for i, num in enumerate(order):
        if i + 1 < len(order) and not is_valid_first(data, num, order[i + 1 :]):
            return False
    return True


def get_match(data, num, arr):
    for val in arr:
        if num in data[val]:
            return val
    return num


def fix_order(data, order):
    j = 0
    # TODO: Better approach instead of n2 is to check
    # if it did not swap at all else skip all computation and
    # increment j+=1
    while j < len(order):
        correct_order, i = [], 0
        while i + 1 < len(order) and len(correct_order) < len(order):
            num = get_match(data, order[i], order[i + 1 :])
            if num != order[i]:
                swap_ind = order.index(num, i + 1)
                order[i], order[swap_ind] = order[swap_ind], order[i]
            correct_order.append(num)
            i += 1
        if len(correct_order) < len(order):
            correct_order.append(order[-1])
        order = correct_order
        j += 1
    return order[len(order) // 2]


def problem_1(contents: str) -> int:
    rules, ordering = contents.split("\n\n")
    data = defaultdict(list)
    for r in rules.splitlines():
        first, second = r.split("|")[0], r.split("|")[1]
        data[int(first)].append(int(second))
    res = []
    for order in ordering.splitlines():
        order = [int(o) for o in order.split(",")]
        if is_valid_order(data, order):
            res.append(order[len(order) // 2])
    return sum(res)


def problem_2(contents: str) -> int:
    rules, ordering = contents.split("\n\n")
    data = defaultdict(list)
    for r in rules.splitlines():
        first, second = r.split("|")[0], r.split("|")[1]
        data[int(first)].append(int(second))
    res = []
    for order in ordering.splitlines():
        order = [int(o) for o in order.split(",")]
        if not is_valid_order(data, order):
            res.append(fix_order(data, order))
    return sum(res)


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
