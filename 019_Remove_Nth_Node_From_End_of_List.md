#  19. 删除链表的倒数第N个节点
* 难度:中等 
## 题目

> 原题链接
* https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/submissions/

> 内容描述

```
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。


```
> example 1 
```
示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

```
> example 2
```

```


## 解题方案
``` 



```

> 我的解答

```python
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #自己写的方式，遍历两遍，第一遍遍历到尾，统计出节点个数l，然后用总结点数l减掉n,得出待删除的节点id,然后删掉。，注意极端情况。[1],1 和 [1,2], 2. 
        l = 0
        tmp = head
        while head:
            l += 1
            head = head.next
        delete_index = l - n
        head = tmp
        if delete_index == 0:
            return head.next
        while delete_index - 1:
            head = head.next
            delete_index -= 1
        pre = head
        delete_node = head.next
        succ = delete_node.next
        pre.next = succ
        return tmp


        
            
```


> 我的解答2

```python
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #参考了官方题解。设置两根指针，当快指针走到n，慢指针再走，这样当快指针走完的时候慢指针也就走到n-1了，然后删除n,方式是将second.next = second.next.next，将要删除的节点的前一个节点的next指向要删节点的下一个。注意：只能走到要删除节点的前一个节点。
        #设置dummy头节点说是防止只有一个节点的极端情况，我还是不是很清楚。
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        while n + 1:
            first = first.next
            n -= 1
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
        

        
            
```