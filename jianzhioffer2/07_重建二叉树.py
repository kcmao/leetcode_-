# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#由前序遍历和中序遍历重建二叉树
def reConstructBinaryTree(pre,tin):
    # 前序 [1,2,4,7,3,5,6,8]
    # 中序 [4,7,2,1,5,3,8,6]
    #使用递归

    if not pre or not tin:
        return None

    value = pre[0]
    id_tin = tin.index(value)
    node = TreeNode(value)

    pre1 = pre[1:id_tin+1]
    tin1 = tin[0:id_tin]

    pre2 = pre[id_tin+1:]
    tin2 = tin[id_tin+1:]

    node.left = reConstructBinaryTree(pre1, tin1)
    node.right = reConstructBinaryTree(pre2,tin2)

    #精髓在这边，没想起来,要时常回顾
    return node


