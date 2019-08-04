# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_path(root, expected_sum):
    if root is None or expected_sum is None:
        return

    current_sum = 0
    path = []
    find_path_core(root, current_sum, expected_sum, path)


def find_path_core(root, current_sum, expected_sum, path):
    #都假定root不是None
    current_sum += root.value
    path.append(root)

    is_leaf = root.left is None and root.right is None
    if is_leaf and current_sum == expected_sum:
        for i in path:
            print(i.value)
        print(" ")
    if root.left:
        find_path_core(root.left, current_sum, expected_sum, path)

    if root.right:
        find_path_core(root.right, current_sum, expected_sum, path)

    path.pop()

if __name__ == "__main__":
    node5 = TreeNode(7)
    node4 = TreeNode(4)
    node3 = TreeNode(12)
    node2 = TreeNode(5, node4, node5)
    node1 = TreeNode(10, node2, node3)
    root = node1
    find_path(root, 22)



