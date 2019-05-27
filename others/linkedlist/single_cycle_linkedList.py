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
length(), travel(), add(), append(), remove(), search()：
    while 判断条件：cur.next == self.__head
    极端情况：空列表：is_empty()  (不需要处理单个元素，其余条件已包含)
"""


class Node(object):
    """
    节点
    """

    def __init__(self, elem):
        self.elem = elem
        self.next = None


# class SingleLinkedList():


class SingleCycleLinkedList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            self.__head.next = self.__head

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """列表长度"""
        # cur游标用来移动遍历节点
        cur = self.__head
        if self.is_empty():
            return 0
        count = 1 #因为用cur.next作为判断条件了，count必须从1开始计数
        #cur == self.__head 不可以作为判断条件，因为压根进不了循环
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """travel all the linkedlist"""
        # 有问题，最后带一个None
        cur = self.__head
        if self.is_empty():
            return
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        #退出循环，cur指向尾节点，但是尾节点元素未打印。
        print(cur.elem, end=' ')

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        #node.next = self.__head
        #为空
        if self.is_empty():
            self.__head = node
            node.next = node
        #不为空，支持单个节点
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            node.next = self.__head    #node指向头节点
            self.__head = node         #把node作为新的self.__head
            # cur.next = self.__head   #将尾节点指向头节点
            cur.next = node            #同上

    def append(self, item):
        """链表尾部添加元素,尾插法"""
        node = Node(item)
        #空
        if self.is_empty():
            self.__head = node
            node.next = node
        #非空 支持单个节点
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next   #将node指向头节点
            cur.next = node        #原尾节点指向node
            # 效果同上
            # cur.next = node
            # node.next = self.__head
    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos 从0开始
        """
        #同单链表，无需任何改动
        if pos <= 0:  # 处理第一种情况，认为是头插
            self.add(item)
        elif pos > self.length() - 1:  # 处理第二种情况，认为是尾插,(注意是大于才是尾插)
            self.append(item)
        else:
            pre = self.__head
            node = Node(item)
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next  # 让pre走到pos位置的前一个位置
            node.next = pre.next  # 先将node的next指向pre.next
            pre.next = node  #

    def remove(self, item):
        """删除指定元素"""
        # 三种极端情况：1，列表空。2删除首节点. 3只有一个节点
        # 用了两个游标
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # 头尾节点删除比较麻烦，其余同单链表。
                if cur == self.__head:
                    #头节点，需要找到尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head  #将尾节点指向新的头节点
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        #删除尾节点情况
        if cur.elem == item:
            pre.next = cur.next


    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        #不空，支持单个节点
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点，但是尾节点元素未打印。需要加一步此操作
        if cur.item == item:
            return True
        return False

if __name__ == "__main__":
    single_cll = SingleCycleLinkedList()
    single_cll.append(1)
    single_cll.append(2)
    single_cll.append(3)
    single_cll.append(4)
    single_cll.append(5)
    print(single_cll.length())
    print(single_cll.travel())
    single_cll.add(6)
    print(single_cll.travel())
    single_cll.insert(-1, 9)
    print(single_cll.travel())
    single_cll.insert(20,100)
    print(single_cll.travel())
    print(single_cll.remove(9))
    print(single_cll.travel())
    print(single_cll.__doc__)

