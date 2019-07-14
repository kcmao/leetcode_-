# -*- coding: utf-8 -*-
"""
面试题18（一）：在O(1)时间删除链表结点
题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该
结点。
输入：头节点和需要删除的节点
返回：头节点
"""

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_node(head_node, delete_node):
    #1,链表是空的
    #2,只有一个节点
    #3,删除的节点在末尾
    #4,删除的节点在中间

    #1
    if head_node is None or delete_node is None:
        return
    #2
    if head_node == delete_node and head_node.next is None:
        return
    #3
    if delete_node.next is None:
        p_node = head_node
        while p_node.next != delete_node:
            p_node = p_node.next
        p_node.next = delete_node.next
        return head_node
    #4
    delete_node.value = delete_node.next.value
    delete_node.next = delete_node.next.next


    return head_node


def test1():
    l1_5 = Node(10)
    l1_4 = Node(7, l1_5)
    l1_3 = Node(5, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head_p = l1_1

    head_p = delete_node(head_p,  l1_2)
    #expect : 1 5 7 10
    print("test1")
    print("expect: 1 5 7 10")
    while head_p is not None:
        print(head_p.value)
        head_p = head_p.next

def test2():
    l1_5 = Node(10)
    l1_4 = Node(7, l1_5)
    l1_3 = Node(5, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head_p = l1_1


    head_p = delete_node(head_p,  l1_5)
    #expect : 1 2 5 7
    print("test2")
    print("expect: 1 2 5 7")
    while head_p is not None:
        print(head_p.value)
        head_p = head_p.next

if __name__ == "__main__":
    test1()
    test2()