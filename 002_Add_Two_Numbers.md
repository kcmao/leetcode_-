#  2. 两数相加
** 难度:   中等**
## 题目

> 原题链接
* https://leetcode-cn.com/problems/add-two-numbers/

> 内容描述

```
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```
> example 1 
```


```
> example 2
```

```


## 解题方案
``` 
遍历两个列表，一次取出其中的值相加，加完重新构造节点并加入新的链表。


```

> 我的解答

```python
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = 0
        num1 = l1
        num2 = l2
        node = head = ListNode(-1)
        while num1 and num2:
            sum_ = num1.val + num2.val + tmp
            tmp = sum_ // 10
            remain = sum_ % 10
            a = ListNode(remain)
            node.next = a
            node = node.next
            num1 = num1.next
            num2 = num2.next
        while num1:
            sum_ = num1.val + tmp
            tmp = sum_ // 10
            remain = sum_ % 10
            a = ListNode(remain)
            node.next = a
            node = node.next
            num1 = num1.next
        while num2:
            sum_ = num2.val + tmp
            tmp = sum_ // 10
            remain = sum_ % 10
            a = ListNode(remain)
            node.next = a
            node = node.next
            num2 = num2.next
        if tmp == 1:
            node.next = ListNode(1)
        return head.next
        

```