# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:30:43 2019

@author: mkc
"""
"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 """
 把链表里的值按顺序放到list中，然后反向打印，很简单，但是肯定不符合要求
 """
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        node_li = []
        node_li_value = []
        node = listNode
        if not node:
            return []
        while node:
            node_li.append(node)
            node_li_value.append(node.val)
            node = node.next
            
        """
        head = cur = node_li.pop()
        while node_li:
            tmp = node_li.pop()
            cur.next = tmp
            cur = tmp
        """
        return node_li_value[::-1]