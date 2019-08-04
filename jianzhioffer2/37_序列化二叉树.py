# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def deserialize(serialize_li):
    if len(serialize_li) == 0:
        return

    if serialize_li[0] == "$":
        node = None
    else:
        node = TreeNode(int(serialize_li[0]))
    serialize_li.pop()

    if node:
        node.left = deserialize(serialize_li)
        node.right = deserialize(serialize_li)
    return node


def serialize(root):
    serialize_li = []
    if root is None:
        return
    serialize_core(root, serialize_li)
    return serialize_li

def serialize_core(root, serialize_li):
    if root is None:
        return
    serialize_li.append(root.value)
    if root.left:
        serialize_core(root.left,serialize_li)
    else:
        serialize_li.append("$")
    if root.right:
        serialize_core(root.right,serialize_li)
    else:
        serialize_li.append("$")

def print_tree_from_top_to_bottom3(root):
    if root is None:
        return

    assert isinstance(root, TreeNode)
    stack1 = []
    stack2 = []
    stack1.append(root)
    level = 1

    while len(stack1) != 0 or len(stack2) != 0:
        if level & 1:
            current_stack = stack1
            next_stack = stack2
        else:
            current_stack = stack2
            next_stack = stack1

        while len(current_stack) != 0:
            node = current_stack.pop()
            print(node.value, end=' ')
            if level & 1:
                if node.left:
                    next_stack.append(node.left)

                if node.right:
                    next_stack.append(node.right)
            else:
                if node.right:
                    next_stack.append(node.right)

                if node.left:
                    next_stack.append(node.left)
        print()
        level += 1



if __name__ == "__main__":
    node6 = TreeNode(6)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node5, node6)
    node2 = TreeNode(2, node4)
    node1 = TreeNode(1, node2, node3)
    root = node1
    print(serialize(root))
    print()
    new_root = deserialize(['1','2','4','$','$','$','3','5','$','$','6','$','$'])

    print_tree_from_top_to_bottom3(new_root)