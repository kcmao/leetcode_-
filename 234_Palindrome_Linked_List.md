#  234. 回文链表
** 难度:  简单 **
## 题目

> 原题链接
* https://leetcode-cn.com/problems/palindrome-linked-list/

> 内容描述

```
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
```
> example 1 
```


```
> example 2
```

```


## 解题方案
``` 
用两根指针，快走两步，慢的走一步，快的走到头的时候，慢的正好走了一半，同时将慢的遍历的值保存，这个时候，慢的继续走，一边走一边和之前保存的对比，如果不相同，直接返回false.
```

> 我的解答

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return True
        fast = head
        slow = head
        values = [head.val]
        flag = 0
        while fast.next:
            if fast.next.next:
                slow = slow.next
                values.append(slow.val)
                fast = fast.next.next
            else:
                #有两种回文情况：奇数个和偶数个，
                #[1,2,3,2,1],当这种情况的时候需要再走一步，value保存了[1,2],slow从3走到2
                #[1,2,2,1]
                flag = 1 
                break
        
        print(values)
        if flag == 1:
            slow = slow.next
        print(slow.val)
        for i in range(1, len(values) + 1):
            if slow.val == values[-i]:
                slow = slow.next
            else:
                return False
        return True
        
        
 
```