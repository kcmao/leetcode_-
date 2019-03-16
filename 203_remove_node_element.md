#  203 移除链表元素
**<font color=red>难度:   </font>**
## 题目

> 原题链接
* 

> 内容描述

```
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
```

## 解题方案
``` 
#两种情况最难，[1] 1 :一定要判断首节点满足的情况，再判空
#[1,2,2, 1] 2 连续两个的情况，不能用pre和cur.
#如果首节点满足，删除首节点，删除空节点情况还必须在空前面，以防单个节点的情况。
链表节点的删除得考虑几种情况：空链表，头节点删除，尾节点删除。循环是否越界


```

> 我的解答

```python
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #两种情况最难，[1] 1 :一定要判断首节点满足的情况，再判空
        #[1,2,2, 1] 2 连续两个的情况，不能用pre和cur.
        #如果首节点满足，删除首节点，删除空节点情况还必须在空前面，以防单个节点的情况。
        while head and head.val == val:
            head = head.next
        #空情况：
        if not head:
            return 
        #其他
        cur = head
        while cur.next:
            if cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return head

        
```