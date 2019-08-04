# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def convert_bstree_to_list(root):
    if root is None:
        return
    node = root
    last_node = None
    last_node = convert_core(node, last_node)

    while last_node.left:
        last_node = last_node.left
    return last_node


def convert_core(node, last_node):
    if node is None:
        return last_node

    node = node
    if node.left:
        last_node = convert_core(node.left, last_node)
    node.left = last_node
    if last_node is not None:
        last_node.right = node
    last_node = node
    if node.right:
        last_node = convert_core(node.right, last_node)
    return last_node


def display(head):
    p = head
    while p:
        print(p.value, end=" ")
        if p.left:
            print(p.left.value, end=" ")
        if p.right:
            print(p.right.value, end=" ")
        print()
        p = p.right


if __name__ == "__main__":
    node7 = TreeNode(16)
    node6 = TreeNode(12)
    node5 = TreeNode(8)
    node4 = TreeNode(4)
    node3 = TreeNode(14, left=node6, right=node7)
    node2 = TreeNode(6, left=node4, right=node5)
    node1 = TreeNode(10, left=node2, right=node3)
    root = node1
    head = convert_bstree_to_list(root)
    display(head)