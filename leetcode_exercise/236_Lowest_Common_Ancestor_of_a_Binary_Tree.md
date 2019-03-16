# 236. 二叉树的最近公共祖先
**<font color=red>难度: 中等</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

> 内容描述

```
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

```



## 解题方案
``` 
抄了https://www.jianshu.com/p/7a2d982c247b，先找到根节点到给定子节点的路径，然后判断两个路径中最后一个相同的元素，就为他们的最近公共祖先。
关键在找路径这边，用递归我绕不过来，不知道用true和false判断。
```

* 首先找到路径
* 
* 


> 1 思路一
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #通过遍历找到根节点到给定节点的路径，注意，要用true 和 false 作为标志，给第三个if作为递归的判断条件，同时用path存储路径，作为路劲栈，如果走错了，回头的时候要将其pop.
        def traversal(root, node, path):
            if not root:
                return False
            path.append(root)
            if root == node:
                return  True     
            if traversal(root.left, node, path) or traversal(root.right, node, path):
                return True
            path.pop()
            return False

        path_p = list()
        path_q = list()
        traversal(root, p, path_p)
        traversal(root, q, path_q)
        #print(path_p, path_q)
        
        i = 0
        while i < len(path_p) and i < len(path_q):
            if path_p[i] != path_q[i]:
                break
            i += 1
        return path_p[i-1]
```
> 2 思路二
```python

```
