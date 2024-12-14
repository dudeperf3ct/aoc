from pathlib import Path

import pytest

TEST_INPUT1 = "2333133121414131402"

EXPECTED_PART1 = 1928

EXPECTED_PART2 = 2858


def read_input_file(file_path: Path = Path("input")):
    with open(file_path, "r") as fp:
        data = fp.read()
    return data


def create_tape1(data):
    files = []
    for i in range(len(data)):
        if i % 2 == 0:
            files.extend([i // 2] * data[i])
    res, i = [], 0
    while len(files) > 0:
        if i % 2 == 0:
            res.extend(files[: data[i]])
            del files[: data[i]]
        elif data[i] != 0:
            res.extend(reversed(files[-data[i] :]))
            del files[-data[i] :]
        i += 1
    return res


def modify_string(orig, out):
    for i, o in enumerate(orig):
        if o == ".":
            break
    orig[i : i + len(out)] = out
    return orig


def create_tape2(data):
    tape = []
    free_space = {}
    for i in range(len(data)):
        if i % 2 == 0:
            tape.append([i // 2] * data[i])
        else:
            free_space[i] = data[i]
            tape.append(["."] * data[i])
    free_space = dict(sorted(free_space.items()))
    i = len(data) - 1
    while i > 0:
        for ind, space in free_space.items():
            if space >= len(tape[i]) and ind < i:
                space -= len(tape[i])
                free_space[ind] = space
                tape[ind] = modify_string(tape[ind], tape[i])
                tape[i] = ["."] * len(tape[i])
                break
        i -= 2
    res = []
    for t in tape:
        res.extend(t)
    return res


def problem_1(contents: str) -> int:
    data = list(contents.strip())
    data = [int(num) for num in data]
    tape = create_tape1(data)
    return sum([i * t for i, t in enumerate(tape)])


def problem_2(contents: str) -> int:
    data = list(contents.strip())
    data = [int(num) for num in data]
    tape = create_tape2(data)
    return sum([i * int(t) for i, t in enumerate(tape) if t != "."])


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT1, EXPECTED_PART1),),
)
def test_part1(test_input: list[str], expected: list[int]) -> None:
    res = problem_1(test_input)
    assert res == expected


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT1, EXPECTED_PART2),),
)
def test_part2(test_input: list[str], expected: list[int]) -> None:
    res = problem_2(test_input)
    assert res == expected


if __name__ == "__main__":
    contents = read_input_file("input")

    answer = problem_1(contents)
    print(answer)

    answer = problem_2(contents)
    print(answer)
