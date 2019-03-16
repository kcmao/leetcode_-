# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:01:44 2019

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
is_empty(),length(),travel(),search同单链表
双链表只用一个游标即可，但是在处理的时候得考虑好前驱后继两种情况
在插入和删除的时候得注意操作顺序
注意极端情况
插入/删除： 头节点/尾节点/空列表/只有一个列表
"""

class Node(object):
    """节点类"""
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None

class DoubleLinkedList(object):
    """双向链表类"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """列表长度"""
        # cur游标用来移动遍历节点
        cur = self.__head
        # count记录数值，初始值设置为0，(为什么不设置1)用来处理极端None情况
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """travel all the linkedlist"""
        # 有问题，最后带一个None
        cur = self.__head
        while cur:
            print(cur.elem, end=' ')
            cur = cur.next

    def add(self, item):
        """链表头部添加元素，头插法"""
        #注意先后顺序,刚开始不能错，后面两种顺序都可以
        node = Node(item)
        node.next = self.__head
        """
        #2
        self.__head.prev = node
        self.__head = node
        """
        #1
        self.__head = node
        node.next.prev = node


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
            node.prev = cur

    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos 从0开始
        """
        # 处理pos两种极端情况：1，pos <= 0 2, pos > length() - 1(注意是大于)
        if pos <= 0:  # 处理第一种情况，认为是头插
            self.add(item)
        elif pos > self.length() - 1:  # 处理第二种情况，认为是尾插,(注意是大于才是尾插)
            self.append(item)
        else:
            cur = self.__head   #不需要pre游标了，用cur即可
            count = 0
            while count < pos : #不用pos - 1
                count += 1
                cur = cur.next  #
            node = Node(item)
            #四步
            node.next = cur.next
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除指定元素"""
        # 三种极端情况：1，列表空。2删除首节点. 3只有一个节点
        cur = self.__head
        while cur:
            if cur.elem == item:
                # 先判断此节点是否是头节点,放在这有点不好，但是不追求效率了
                if cur == self.__head:         #处理删除头节点。
                    self.__head = cur.next
                    if cur.next:               #判断列表是否只有一个节点
                        cur.next.prev = None   #头节点的前驱需要置空
                else:
                    #两句话
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
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
    double_ll = DoubleLinkedList()
    print(double_ll.is_empty())
    print(double_ll.length())
    double_ll.append(1)
    print(double_ll.is_empty())
    print(double_ll.length())
    double_ll.append(2)
    double_ll.append(3)
    double_ll.append(4)
    double_ll.append(5)
    print(double_ll.length())
    print(double_ll.travel())  #failed 每次都会多输出一个None
    double_ll.add(6)
    print(double_ll.travel())
    double_ll.insert(-1, 9)
    print(double_ll.travel())
    double_ll.insert(20, 100)
    print(double_ll.travel())
    print(double_ll.length())
    print(double_ll.remove(100))
    print(double_ll.travel())
    print(double_ll.remove(1))  #failed 每次都会输出一个None
    print(double_ll.travel())
