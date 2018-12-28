# 144.  二叉树的前序遍历 
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

> 内容描述

```
给定一个二叉树，返回它的 前序 遍历。

Example 1:
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
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
* beats 97%   60ms
```python
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return []
        else:
            self.preorder(root, res)
            return res
        
        
              
    def preorder(self, root, res):
        if root == None:
            return 
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res) 
```
> 迭代
```
执行用时: 44 ms, 在Binary Tree Preorder Traversal的Python3提交中击败了97.73% 的用户。
思想：result保存遍历结果。
      stack作为栈。
程序思路：
     1.根节点入栈，
     2.判断栈是否为空，
        2.1为空：退出，返回result
        2.2不为空，栈弹出一个到result,右孩子入栈，左孩子入栈。
     3.重复2

     一般过程为：1->2.2->2.2->...->2.1 结束

```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []       #栈
        res = []
        if root:
            stack.append(root)
        while stack:
            x = stack.pop()
            res.append(x.val)
            if x.right:
                stack.append(x.right)  #右节点先进后出
            if x.left:
                stack.append(x.left)   #左节点后进先出
        return res
```
> 迭代法2
* 见05-E2-1
```python
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def visitAlongLeftBranch(x, res, s):
            while x:
                res.append(x.val)
                s.append(x.right)
                x = x.left
        s = []
        res = []
        while True:
            visitAlongLeftBranch(root, res, s)
            if not s:
                break
            root = s.pop()
        return res
```

```
上面等价于下面，只是写法不一样。思想是把整个先序遍历抽象成1，访问左子树.2，将右子树入栈。

```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        res = []
        while True:
            self.visitAlongLeftBranch(root, res, s)
            if not s:
                break
            root = s.pop()
        return res
        
    def visitAlongLeftBranch(self,x, res, s):
        while x:
            res.append(x.val)
            s.append(x.right)
            x = x.left  
```