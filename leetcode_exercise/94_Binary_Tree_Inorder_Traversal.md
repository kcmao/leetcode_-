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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorder(root, res)
        return res        
        
        
    def inorder(self, root, res):
        if not root:
            return 
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res) 
```
> 2 迭代
```
执行用时: 44 ms, 在Binary Tree Preorder Traversal的Python3提交中击败了97.73% 的用户。
思想：递归不再是尾递归，思路差不多。
    首先：申明一个res保存结果，stack作为栈。
    定义一个goAlongLeftBranch目的为将树的左节点全部入栈，知道没有左节点，然后stack弹出一个x,visit(x),然后对右节点重复以上动作。
    注：visit(x)即：res.append(x)

```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while True:
            self.goAlongLeftBranch(root, stack, res)
            if not stack:
                break
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
        
        
    def goAlongLeftBranch(self, x, s, res):
        while x:
            s.append(x)
            x = x.left
        
        
        
        
```
