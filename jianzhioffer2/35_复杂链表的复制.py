# -*- coding: utf-8 -*-
class ComplexNode(object):
    def __init__(self, value, next=None, sibling=None):
        self.value = value
        self.next = next
        self.sibling = sibling

def clone_complex_link(head):

    insert_next(head)
    connect_sibling_nodes(head)
    return reconnect_node(head)

#链表后面添加节点
def insert_next(head):
    node = head
    while node:
        clone_node = ComplexNode(node.value+"'")
        clone_node.next = node.next
        node.next = clone_node
        node = clone_node.next




#连接上sibling节点
def connect_sibling_nodes(head):
    node = head
    while node :        #注意
        clone_node = node.next
        if node.sibling:
            clone_node.sibling = node.sibling.next
        node = clone_node.next


def reconnect_node(head):
    node = head
    clone_node = head.next
    clone_head = clone_node

    node.next = clone_node.next
    node = clone_node.next

    while node:
        clone_node.next = node.next
        clone_node = node.next

        node.next = clone_node.next
        node = clone_node.next

    return clone_head


def display(head):
    if not isinstance(head, ComplexNode):
        return
    p = head
    while p:
        print(p.value, end=" ")
        if p.next:
            print(p.next.value, end=" ")
        if p.sibling:
            print(p.sibling.value, end=" ")
        print()
        p = p.next

if __name__ == "__main__":
    node5 = ComplexNode('E')
    node4 = ComplexNode('D', next=node5)
    node3 = ComplexNode('C', next=node4)
    node2 = ComplexNode('B', next=node3)
    node1 = ComplexNode('A', next=node2)
    node1.sibling = node3
    node2.sibling = node5
    node4.sibling = node2
    head = node1
    display(head)
    print("haha")

    clone_head = clone_complex_link(head)
    display(head)
    print("haha")
    display(clone_head)




