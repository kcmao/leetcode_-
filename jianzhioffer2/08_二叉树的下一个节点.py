# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, value, parent=None,left=None, right=None):
        self.val = value
        self.parent = parent
        self.left = left
        self.right = right

def set_relation(parent, left, right):
    parent.left = left
    parent.right = right
    left.parent = parent
    right.parent = parent

def find_next_node_in_inordered(node):
    """
    给定树中一个节点，返回该节点在中序遍历中的下一个节点
    :param node:
    :return:
    """
    if node is None:
        return None

    #1,如果一个节点有右子树，则下一个节点是右子树的最左子节点,如果右子树就一个点，那就是着一个点
    #2,如果一个节点没有右子树：
        #1,他是他父亲的左子节点：下一个节点就是他父亲。
        #2,他是他父亲的右子节点: 下一个节点是向上找父亲，找到没有父亲的那
            #个节点，如果是他的左孩子，那这个父亲就是下一个节点
    #1
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    #2
    else:
        #2.1
        if node == node.parent.left:
            return node.parent
        #2.2
        else:
            while node.parent:
                node_b = node
                node = node.parent
            if node_b == node.left:
                return node
            return None

if __name__ == "__main__":
    node_i = TreeNode("i")
    node_h = TreeNode("h")
    node_g = TreeNode("g")
    node_f = TreeNode("f")
    node_e = TreeNode("e")
    node_d = TreeNode("d")
    node_c = TreeNode("c")
    node_b = TreeNode("b")
    node_a = TreeNode("a")
    set_relation(node_e, node_h, node_i)
    set_relation(node_c, node_f, node_g)
    set_relation(node_b, node_d, node_e)
    set_relation(node_a, node_b, node_c)

    print(find_next_node_in_inordered(node_f).val)