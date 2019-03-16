#  
**<font color=red>难度:中等   </font>**
## 题目

> 原题链接
* https://leetcode-cn.com/problems/odd-even-linked-list/

> 内容描述

```

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

```

## 解题方案
``` 
设置两个游标even和odd,画图，注意几种不同的用例。


```

> 我的解答

```python
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        dummy_even = even = head.next
        while True:
            if even.next:       #只有偶数个节点
                odd.next = even.next
                odd = odd.next
                if odd.next:   #只有奇数个节点
                    even.next = odd.next
                    even = even.next
                else:
                    even.next = None
                    break
            else:
                break
        odd.next = dummy_even
        return head
    
```