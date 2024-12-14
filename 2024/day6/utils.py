class WalkGrid:
    def __init__(self, data):
        self.grid = {
            (row_no, col_no): char
            for row_no, row in enumerate(data)
            for col_no, char in enumerate(row)
        }
        self.guard_pos = None
        self.move_direction = None
        self.row_len = len(data)
        self.col_len = len(data[0])
        self.get_guard_pos()
        self.direction = ""

    def get_guard_pos(self):
        for index, val in self.grid.items():
            if val == "^":
                self.guard_pos = index
                self.move_direction = index[0] - 1, index[1]
                self.direction = val
                break
            if val == ">":
                self.guard_pos = index
                self.move_direction = index[0], index[1] + 1
                self.direction = val
                break
            if val == "<":
                self.guard_pos = index
                self.move_direction = index[0], index[1] - 1
                self.direction = val
                break
            if val == "v":
                self.guard_pos = index
                self.move_direction = index[0] + 1, index[1]
                self.direction = val
                break

    def do_turn(self, next_index):
        current_pos = self.guard_pos
        # print("curr pos:", current_pos)
        # going up
        if current_pos[0] == next_index[0] + 1 and current_pos[1] == next_index[1]:
            new_index = current_pos[0], current_pos[1] + 1
            # print("going up: ", current_pos, new_index, self.grid[new_index])
            # TOOD: what if there's a # at new index?
            if self.grid[new_index] == "." or self.grid[new_index] == "X":
                self.grid[new_index] = ">"
                self.grid[current_pos] = "X"
        # going down
        if current_pos[0] == next_index[0] - 1 and current_pos[1] == next_index[1]:
            new_index = current_pos[0], current_pos[1] - 1
            # print("going down : ", new_index, self.grid[new_index])
            # TOOD: what if there's a # at new index?
            if self.grid[new_index] == "." or self.grid[new_index] == "X":
                self.grid[new_index] = "<"
                self.grid[current_pos] = "X"
        # going right
        if current_pos[0] == next_index[0] and current_pos[1] == next_index[1] - 1:
            new_index = current_pos[0] + 1, current_pos[1]
            # print("going right: ", new_index, self.grid[new_index])
            # TOOD: what if there's a # at new index?
            if self.grid[new_index] == "." or self.grid[new_index] == "X":
                self.grid[new_index] = "v"
                self.grid[current_pos] = "X"
        # going left
        if current_pos[0] == next_index[0] and current_pos[1] == next_index[1] + 1:
            new_index = current_pos[0] - 1, current_pos[1]
            # print("going left: ", new_index, self.grid[new_index])
            # TOOD: what if there's a # at new index?
            if self.grid[new_index] == "." or self.grid[new_index] == "X":
                self.grid[new_index] = "^"
                self.grid[current_pos] = "X"

    def one_step(self):
        try:
            current_pos = self.guard_pos
            next_index = self.move_direction
            # print(current_pos, next_index, self.move_direction, self.grid[next_index])
            if (
                0 < next_index[0] < self.row_len
                and 0 < next_index[1] < self.col_len
                and (self.grid[next_index] == "." or self.grid[next_index] == "X")
            ):
                self.grid[next_index] = self.grid[current_pos]
                self.grid[current_pos] = "X"
                self.guard_pos = next_index
            elif (
                0 <= next_index[0] < self.row_len
                and 0 <= next_index[1] < self.col_len
                and self.grid[next_index] == "#"
            ):
                # print("do turn", next_index)
                self.do_turn(next_index)
            self.get_guard_pos()
        except KeyError:
            return True

    def print_grid(self):
        for row in range(self.row_len):
            line = "".join(self.grid[(row, col)] for col in range(self.col_len))
            print(line)

    def walk_grid(self):
        i = 0
        flag = False
        # Run this for a large number of times
        # Better way to detect loop?
        while i < 1_000_000:
            flag = self.one_step()
            if flag:
                return
            # self.print_grid()
            i += 1

    def count_distinct_place(self):
        res = 0
        for _, val in self.grid.items():
            if val == "X" or val in ["<", ">", "v", "^"]:
                res += 1
        return res


if __name__ == "__main__":
    d = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]
    g = WalkGrid(d)
    g.walk_grid()
    print(g.count_distinct_place())
