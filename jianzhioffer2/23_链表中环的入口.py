# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
"""
第一个节点一次走两步，第二个节点一次走一步，然后相遇的时候就是说明有环，
然后第一个节点继续走，遇到第二个节点的时候就是环的长度，

然后两个节点重新从头开始走，一个先走环的长度，然后两个相遇的时候就是环的入口。
"""

def meetingNodes(Node):
    if Node is None:
        return
    if Node.next is None:
        return

    first = Node
    second = Node

    flag = 0
    while first.next.next:
        first = first.next.next
        second = second.next
        if first == second:
            flag = 1
            break

    if flag == 0:
        return

    node_num = 0

    while True:
        first = first.next
        node_num += 1
        if first == second:
            break

    first = Node
    second = Node

    for i in range(node_num):
        first = first.next

    while first != second:
        first = first.next
        second = second.next

    return first




def Test1():

    l1_6 = Node(6)
    l1_5 = Node(5, l1_6)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    l1_2.next = l1_1
    head = l1_1
    print(meetingNodes(head).value)



if __name__ == "__main__":
    Test1()













