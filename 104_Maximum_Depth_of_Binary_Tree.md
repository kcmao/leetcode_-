# 104.   二叉树的最大深度
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/submissions/

> 内容描述

```
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
Example 1:
示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7

```



## 解题方案
``` 
用递归，然后比较左右递归的深度，每次递归进去，返回的时候深度加一，

自己其实并不是很理解，抄的别人的解答，总之，要好好理解递归，递归主要是要递归进去，又要重新返回，注意里面的那么对return。
```

> 1 递归
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            leftdepth = self.maxDepth(root.left)
            rightdepth = self.maxDepth(root.right)
            if leftdepth < rightdepth:
                return rightdepth + 1
            else:
                return leftdepth + 1
        else:
            return 0
```