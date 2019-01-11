#  142. 环形链表 II
**<font color=red>难度: 中等</font>**
## 题目

> 原题链接
* https://leetcode-cn.com/problems/linked-list-cycle-ii/submissions/

> 内容描述

```
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
不允许修改给定的链表。
```
> example 1 
```
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点

```
> example 2
```
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
```


## 解题方案
``` 

别人都是快慢指针，我觉得直接用list保存已经存在的node，遍历其next，如果在list中，则输出node,否则遍历结束输出None。不过只击败了3%的用户，可能快慢指针够快吧。

```

> 我的解答

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        nodes = {}
        while head:
            if head in nodes:
                return True
            nodes[head] = 1
            head = head.next
        return False  
```