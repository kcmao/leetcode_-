# 112.   路径和
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/path-sum/

> 内容描述

```
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

```



## 解题方案
``` 
递归进入树，保存一个零时和tmp_sum,每进入一次递归，做三个分支的判断，关键时如何找到递归基即退出递归的方式，满足两个其一
1.node不存在，不可或缺，
2.没有了左右孩子时再判断sum是否满足。
    有左右孩子时如何进入，and和or的使用
网上更好的方式时递减的思路，sum-node.val，见思路二
```

* 一，判断节点是否存在，（不能缺少）
* 二，判断如果左右子树存在其一的时候就继续递归下去，
* 三，当以上都不满足时即节点存在同时没有了左右孩子，这时候返回tmp_sum和sum是否相等，


> 1 递归
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #就是类似于先序遍历的例子

        
        def preOrder(node, tmp_sum, sum):
            if not node:                  
                return False
            tmp_sum += node.val
            if node.left or node.right: #or运算符如果前面满足就执行先前面，后面就不管，如果前面不满足就执行后面表达式
                return preOrder(node.left, tmp_sum, sum) or preOrder(node.right, tmp_sum, sum)
            else:
                return tmp_sum == sum     
                                                                     
        tmp_sum = 0                                                                 
        if not root:
            return False
        else:
            return preOrder(root, tmp_sum, sum)
```
> 2 减法
```python
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left or root.right:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        else:
            return root.val == sum 

```
