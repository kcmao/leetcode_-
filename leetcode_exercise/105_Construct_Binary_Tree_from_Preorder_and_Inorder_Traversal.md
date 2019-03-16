# 105.   从前序与中序遍历序列构造二叉树
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

> 内容描述

```
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

```



## 解题方案
``` 
前序加中序，关键是前序的根节点是第一个元素，只要找到中序中对应的前序的第一个节点位置，然后将其分开成两份继续递归即可。
难点在于退出递归的条件和返回的是什么。最后应该返回的是一个节点。但是通过这个节点，我可以找到所有节点和树的关系。
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        index = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
```