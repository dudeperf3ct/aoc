from collections import deque


class TreeNode:
    def __init__(self, num, index):
        self.num = num
        self.index = index


def eval_numbers(output, numbers, use_concat=False):
    root_node = TreeNode(num=numbers[0], index=0)
    queue = deque([root_node])
    while queue:
        curr_node = queue.popleft()
        if curr_node.index == len(numbers) - 1:
            if curr_node.num == output:
                return output
            continue

        next_index = curr_node.index + 1
        next_num = numbers[next_index]

        add_value = curr_node.num + next_num
        queue.append(TreeNode(num=add_value, index=next_index))

        mul_value = curr_node.num * next_num
        queue.append(TreeNode(num=mul_value, index=next_index))

        if use_concat:
            concat_value = int(f"{curr_node.num}{next_num}")
            queue.append(TreeNode(num=concat_value, index=next_index))
    return 0
