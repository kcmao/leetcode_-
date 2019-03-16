#  430. 扁平化多级双向链表
** 难度:  中等 **

> 原题链接
* https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/

> 内容描述

```
您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。

 

示例:

输入:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

输出:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
```
> example 1 
```


```
> example 2
```

```


## 解题方案
``` 
我首先想到是这是一颗二叉树，child是左节点，next是右节点,先先序遍历得出所有节点的值，然后再重建双向链表，虽然很蠢，但是简单，实际上用栈保存子节点，然后添加到主干上比较好。


```

> 我的解答

```python
 """
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return 
        order = []
        def preorder(head, order):
            if not head:
                return 
            order.append(head.val)
            preorder(head.child, order)
            preorder(head.next, order)
        preorder(head, order)
        #上面为先序遍历的结果，等于要求的顺序。然后再重建链表。
        #print(order)
        head = prev = None
        node_li = []
        for val in order:
            node = Node(val, prev=None, next=None, child=None)
            node_li.append(node)  #先重建，再添加next和prev属性。          
        for i in range(len(node_li)-1):
            node_li[i].next = node_li[i+1]
            node_li[i+1].prev = node_li[i]
        return node_li[0]
        
            
```