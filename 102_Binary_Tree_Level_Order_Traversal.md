# 144.  二叉树的层次遍历 
**<font color=red>难度: 中等</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

> 内容描述

```
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

Example 1:
Input: [1,null,2,3]
     3
   / \
  9  20
    /  \
   15   7

[
  [3],
  [9,20],
  [15,7]
]
```


## 解题方案
``` 
递归
 
```

> 1 有问题，自己写的

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None

from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = deque()
        q.append(root)
        while q:
            x = q.popleft()
            res.append(x.val)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        return res
             
```
```
输入：[3,9,20,null,null,15,7]
输出：[3,9,20,15,7]
预期结果：[[3],[9,20],[15,7]]
```

写的不对，但是我又不会改。不知道如何控制深度去控制添加[]. 

> 递归解法 看了别人的
```
用level控制层级，两层递归的执行执行顺序一定要搞懂。
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, level, res):
            if not node:
                return
            if len(res) < level: #用判断res长度的方法给res添加[],达到list添加list的效果。
                res.append([])  #不加if代码块，那就和上面一样
            res[level-1].append(node.val)
            dfs(node.left, level+1, res)
            dfs(node.right, level+1, res)

        res = []
        dfs(root, 1, res)
        return res
```

