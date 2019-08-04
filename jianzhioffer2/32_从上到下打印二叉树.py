class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_top_to_bottom(root):
    if root is None:
        return []
    queue = []
    res = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        res.append(node.val)
    return res


def print_top_to_bottom_layer(root):

    if root is None:
        return []
    queue = []
    res = []
    depth = 0
    queue.append([root, depth])

    while queue:
        node = queue.pop(0)

        depth = node[1]
        value = node[0]

        if depth > len(res) - 1:
            res.append([])

        if value.left:
            queue.append([value.left,depth+1])
        if value.right:
            queue.append([value.right, depth+1])

        res[depth].append(value)
    return res

def print_value_layer(res):
    for layer in res:
        for node in layer:
            print(node.value, end=" ")
        print()

def print_top_to_bottom_zhi(root):
        return print_top_to_bottom_layer(root)
def print_value_zhi(res):
    for index, layer in enumerate(res):
        if index % 2 == 0:
            for node in layer:
                print(node.value, end=" ")
        else:
            for node in layer[::-1]:
                print(node.value, end=" ")
        print()









if __name__ == "__main__":
    node7 = TreeNode(11)
    node6 = TreeNode(9)
    node5 = TreeNode(7)
    node4 = TreeNode(5)
    node3 = TreeNode(10, left=node6, right=node7)
    node2 = TreeNode(6, left=node4, right=node5)
    node1 = TreeNode(8, left=node2, right=node3)
    root = node1
    #print_top_to_bottom(root)

    res = print_top_to_bottom_layer(root)
    print_value_layer(res)

    res = print_top_to_bottom_zhi(root)
    print_value_zhi(res)
