# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_list(head1, head2):
    node1 = head1
    node2 = head2

    if head1 is None and head2 is None:
        return

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    new_node = Node(-1)
    new_head = new_node

    while node1 and node2:
        if node1.value < node2.value:
            new_node.next = node1
            node1 = node1.next
            new_node = new_node.next
        else:
            new_node.next = node2
            node2 = node2.next
            new_node = new_node.next

    if node1:
        new_node.next = node1
    else:
        new_node.next = node2

    return new_head.next


if __name__ == "__main__":
    l1_5 = Node(10)
    l1_4 = Node(7, l1_5)
    l1_3 = Node(5, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)

    l2_3 = Node(6)
    l2_2 = Node(6, l2_3)
    l2_1 = Node(5, l2_2)
    l1_1 = merge_list(l1_1, l2_1)

    while l1_1 is not None:
        print(l1_1.value)
        l1_1 = l1_1.next





