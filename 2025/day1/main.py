from pathlib import Path

import pytest

TEST_INPUT = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

EXPECTED_PART1 = 3

EXPECTED_PART2 = 6


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


def part1(contents: str, start_pos: int = 50) -> int:
    dial = start_pos
    count = 0
    for line in contents.splitlines():
        direction = line[0]
        num = int(line[1:])
        if direction == "L":
            num *= -1
        dial = (dial + num) % 100
        if dial == 0:
            count += 1
    return count


def part2(contents: str, start_pos: int = 50) -> int:
    # Brute force
    dial = start_pos
    count = 0
    for line in contents.splitlines():
        direction = line[0]
        num = int(line[1:])
        for i in range(num):
            if direction == "L":
                dial -= 1
            else:
                dial += 1
            dial %= 100
            if dial == 0:
                count += 1
    return count


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT, EXPECTED_PART1),),
)
def test_part1(test_input: str, expected: int) -> None:
    assert part1(test_input) == expected


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT, EXPECTED_PART2),),
)
def test_part2(test_input: str, expected: int) -> None:
    assert part2(test_input) == expected


if __name__ == "__main__":
    contents = read_input_file("input")

    answer = part1(contents)
    print(answer)

    answer = part2(contents)
    print(answer)
