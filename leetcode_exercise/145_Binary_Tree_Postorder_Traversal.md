# 144.  二叉树的中序遍历 
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

> 内容描述

```
给定一个二叉树，返回它的中序 遍历。

Example 1:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```
> 注意
```
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
```


## 解题方案
``` 
递归很简单，
 


```

> 1 递归
* beats 40%   56ms
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            self.postorder(root, res)
        return res
        
        
    def postorder(self, root, res):
        while not root:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val) 
```

