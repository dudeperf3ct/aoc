class SearchWord:
    def __init__(self, data, word="XMAS"):
        self.grid = {
            (row_no, col_no): char
            for row_no, row in enumerate(data)
            for col_no, char in enumerate(row)
        }
        self.row_len = len(data)
        self.col_len = len(data[0])
        self.word_len = len(word)
        self.word = word
        self.directions = [
            (0, 1),  # right
            (0, -1),  # left
            (1, 0),  # down
            (-1, 0),  # up
            (-1, 1),  # right-up diagonal
            (1, 1),  # right-down diagonal
            (-1, -1),  # left-up diagonal
            (1, -1),  # left-down diagonal
        ]

    def check_direction(self, index, delta_row, delta_col):
        row, col = index
        word = "".join(
            self.grid.get((row + i * delta_row, col + i * delta_col), "")
            for i in range(self.word_len)
        )
        if word == self.word or word[::-1] == self.word:
            return 1
        return 0

    def check_all_directions(self, index):
        return sum(self.check_direction(index, dr, dc) for dr, dc in self.directions)

    def count_word(self):
        return sum(
            self.check_all_directions(index)
            for index, char in self.grid.items()
            if char == "X"
        )

    def count_xmas(self):
        res = 0
        for index, char in self.grid.items():
            if char == "A":
                row, col = index
                top = [
                    self.grid.get((row - 1, col - 1), ""),
                    self.grid.get((row - 1, col + 1), ""),
                ]
                bottom = [
                    self.grid.get((row + 1, col - 1), ""),
                    self.grid.get((row + 1, col + 1), ""),
                ]
                if "MS" in "".join(top) and "MS" in "".join(bottom):
                    res += 1
                if "SM" in "".join(top) and "SM" in "".join(bottom):
                    res += 1
                elif "MM" in "".join(top) and "SS" in "".join(bottom):
                    res += 1
                elif "SS" in "".join(top) and "MM" in "".join(bottom):
                    res += 1
        return res
