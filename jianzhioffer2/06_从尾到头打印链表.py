# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def print_list_reverse(head):
    """
    用栈实现，鲁棒性较好
    :param head:
    :return:
    """
    if head is None:
        return

    stack = []
    node = head

    while node:
        stack.append(node)
        node = node.next

    while len(stack):
        print(stack.pop().value)

def print_list_reverse2(head):
    """
    递归实现
    :param head:
    :return:
    """
    if head is None:
        return
    print_list_reverse2(head.next)
    print(head.value)

if __name__ == "__main__":
    n5 = Node(value=5)
    n4 = Node(value=4, next=n5)
    n3 = Node(value=3, next=n4)
    n2 = Node(value=2, next=n3)
    head = Node(value=1, next=n2)
    print_list_reverse(head)
    print_list_reverse2(head)



