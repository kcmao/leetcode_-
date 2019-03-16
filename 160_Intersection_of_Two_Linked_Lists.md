#  160. 相交链表
**<font color=red>难度:简单  </font>**
## 题目

> 原题链接
* https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

> 内容描述

```
编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：
```
详见题目链接


## 解题方案
``` 
用 list存储一条链表所有节点，然后访问另一条链表的节点，并判断是否在list中，如果在，返回即可，击败了全国1%的人。差点没超时间限制。
```

> 我的解答

```python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node_list = []
        while headA:
            node_list.append(headA)
            headA = headA.next
        headBB = headB
        '''
        for node in node_list:
            headB = headBB
            while headB:
                if headB == node:
                    return headB
                headB = headB.next
        '''
        while headB:
            if headB in node_list:
                return headB
            headB = headB.next
        return
        
 
```