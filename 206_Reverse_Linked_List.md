#  206. 反转链表
**<font color=red>难度:简单 </font>**
## 题目

> 原题链接
* https://leetcode-cn.com/problems/reverse-linked-list/

> 内容描述

```
反转一个单链表。
```
> example 1 
```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

```


## 解题方案
```   
三根指针，分别是previous，current， next
方法是将cur指向(pre)None,然后三个节点分别向后移动一位，即每次将指针向后指一个。
完全不同于上面说的方法，这个简单多了，又好理解，又好操作。


```

> 我的解答

```python
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        比如 1 2 3调换位置 2 1 3   
        三根指针，分别是previous，current， next
        方法是将cur指向(pre)None,然后三个节点分别向后移动一位，即每次将指针向后指一个。
        完全不同于上面说的方法，这个简单多了，又好理解，又好操作。
        '''
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

```