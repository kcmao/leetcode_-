#116. 填充同一层的兄弟节点
**<font color=red>难度: 中等</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/submissions/

> 内容描述

```
给定一个二叉树

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

说明:

你只能使用额外常数空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。
示例:

给定完美二叉树，

     1
   /  \
  2    3
 / \  / \
4  5  6  7
调用你的函数后，该完美二叉树变为：

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
```



## 解题方案
``` 
树的层序遍历，将遍历的结果保存在list中，然后循环遍历这个list,添加next节点，广度遍历的方法直接参考了102题。
```

> 1 递归
```python
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def dfs(node, level, res):
            if not node:
                return
            if len(res) < level:
                res.append([])
            res[level-1].append(node)
            dfs(node.left, level+1, res)
            dfs(node.right, level+1, res)
                                
        if not root:
            return 
        else:
            res = []
            dfs(root, 1, res)
            for node_li in res:
                for i in range(len(node_li) - 1):
                    node_li[i].next = node_li[i+1] 
```