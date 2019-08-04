# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

"""
三根指针，注意将nxt指针放到while循环里第一个位置，这样就保证next指针不越界了。
"""

def reverse_link_list(head):
    if head is None:
        return
    if head.next is None:
        return head


    pre = None
    node = head

    while node:

        nxt = node.next
        node.next = pre
        pre = node
        node = nxt


    return pre


if __name__ == "__main__":
    l1_6 = Node(6)
    l1_5 = Node(5, l1_6)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head = l1_1
    p = reverse_link_list(head)
    while p:
        print(p.value)
        p = p.next
