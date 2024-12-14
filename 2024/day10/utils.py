from collections import deque


class Grid:
    def __init__(self, data):
        self.grid = {
            (row_no, col_no): int(val) if val != "." else -1
            for row_no, row in enumerate(data)
            for col_no, val in enumerate(row)
        }
        self.directions = [
            (0, 1),  # right
            (0, -1),  # left
            (1, 0),  # down
            (-1, 0),  # up
        ]

    def get_all_directions(self, index):
        row, col = index
        pos = []
        for dr, dc in self.directions:
            pos.append((row + dr, col + dc))
        return [(p, self.grid.get(p, "")) for p in pos]


class TreeNode:
    def __init__(self, num, pos):
        self.num = num
        self.pos = pos

    def __repr__(self):
        return f"num={self.num}, pos={self.pos}"


def find_heads_tails(grid) -> list[tuple[int, int]]:
    heads, tails = [], []
    for pos, val in grid.items():
        if val == 0:
            heads.append(pos)
        if val == 9:
            tails.append(pos)
    return heads, tails


def traverse_trail(data):
    g = Grid(data)
    grid = g.grid
    heads, tails = find_heads_tails(grid)
    ans = 0
    for pos in heads:
        res = dict.fromkeys(tails, 0)
        root_node = TreeNode(grid[pos], pos)
        queue = deque([root_node])
        while queue:
            curr_node = queue.popleft()
            curr_pos = curr_node.pos
            curr_num = curr_node.num

            all_pos = g.get_all_directions(curr_pos)
            if curr_num + 1 == 9:
                all_9_pos = g.get_all_directions(curr_pos)
                for dir in all_9_pos:
                    p, v = dir
                    if v == 9:
                        res[p] += 1
            else:
                for dir in all_pos:
                    pos, val = dir
                    if val != "" or val != -1:
                        if val == curr_num + 1:
                            queue.append(TreeNode(val, pos))
        ans += sum(1 for _, v in res.items() if v > 0)
    return ans


def traverse_trail1(data):
    g = Grid(data)
    grid = g.grid
    heads, _ = find_heads_tails(grid)
    ans = 0
    for pos in heads:
        res = dict.fromkeys(range(10), 0)
        root_node = TreeNode(grid[pos], pos)
        queue = deque([root_node])
        while queue:
            curr_node = queue.popleft()
            curr_pos = curr_node.pos
            curr_num = curr_node.num

            all_pos = g.get_all_directions(curr_pos)
            for dir in all_pos:
                pos, val = dir
                if val != "" or val != -1:
                    if val == curr_num + 1:
                        queue.append(TreeNode(val, pos))
                        res[val] += 1
        ans += res[9]
    return ans


if __name__ == "__main__":
    i = """\
012345
123456
234567
345678
4.6789
56789.
"""
    d = i.splitlines()
    traverse_trail1(d)
