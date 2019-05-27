# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:01:44 2019

@author: mkc
"""
"""
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""

"""
注意 = 和 .next = 
注意两个游标：cur和pre和next
注意两种判断条件：
    cur != None : length(), travel(), search(), remove() 
    cur.next != None : add()
注意，插入：处理节点的先后顺序：先处理待插的节点的next(不破坏原列表),然后再处理原列表。
"""

class Node(object):
    """
    节点
    """
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        
#class SingleLinkedList():
    

class SingleLinkedList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """列表长度"""
        # cur游标用来移动遍历节点
        # 包含判空，所以不需要单独判空
        cur = self.__head
        # count记录数值，初始值设置为0，(为什么不设置1)用来处理极端None情况
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """travel all the linkedlist"""
        #有问题，最后带一个None
        cur = self.__head
        while cur:
            print(cur.elem, end=' ')
            cur = cur.next

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node


    def append(self, item):
        """链表尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos 从0开始
        """
        #处理pos两种极端情况：1，pos <= 0 2, pos > length() - 1(注意是大于)
        if pos <= 0: #处理第一种情况，认为是头插
            self.add(item)
        elif pos > self.length() -1: #处理第二种情况，认为是尾插,(注意是大于才是尾插)
            self.append(item)
        else:
            pre = self.__head
            node = Node(item)
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next   #让pre走到pos位置的前一个位置
            node.next = pre.next #先将node的next指向pre.next
            pre.next = node      #


    def remove(self, item):
        """删除指定元素"""
        #三种极端情况：1，列表空。2删除首节点. 3只有一个节点
        #用了两个游标
        cur = self.__head
        pre = None
        while cur:
            if cur.elem == item:
                #先判断此节点是否是头节点,放在这有点不好，但是不追求效率了
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    single_ll = SingleLinkedList()
    print(single_ll.is_empty())
    print(single_ll.length())
    single_ll.append(1)
    print(single_ll.is_empty())
    print(single_ll.length())
    single_ll.append(2)
    single_ll.append(3)
    single_ll.append(4)
    single_ll.append(5)
    print(single_ll.length())
    print(single_ll.travel())
    single_ll.add(6)
    print(single_ll.travel())
    single_ll.insert(-1, 9)
    print(single_ll.travel())
    single_ll.insert(20,100)
    print(single_ll.travel())
    print(single_ll.length())
    print(single_ll.remove(100))
    print(single_ll.travel())