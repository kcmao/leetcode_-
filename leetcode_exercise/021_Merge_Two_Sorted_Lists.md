# 21. 合并两个有序链表 
** 难度: 简单  **
## 题目

> 原题链接
* https://leetcode-cn.com/problems/merge-two-sorted-lists/

> 内容描述

```
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```
> example 1 
```


```
> example 2
```

```


## 解题方案
``` 
就是归并排序的归并部分


```

> 我的解答

```python
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        #当一个空了的时候，直接将next指向另一个 
        cur.next = l1 if l1 else l2
        return dummy.next
        

```