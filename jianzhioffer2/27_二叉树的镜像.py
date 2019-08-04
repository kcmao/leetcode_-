# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#二叉树不对称怎么办，没关系，哪怕一个节点的子树其中一个是空，我照样交换
def mirror_recursively(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return

    tmp = root.left
    root.left = root.right
    root.right = tmp

    mirror_recursively(root.left)
    mirror_recursively(root.right)