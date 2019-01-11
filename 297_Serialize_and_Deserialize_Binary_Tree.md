# 297. 二叉树的序列化与反序列化 
**<font color=red>难度: 困难</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

> 内容描述

```
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的
```


## 解题方案
``` 
题目意思是你不管你用什么方式将一颗二叉树序列化，然后再将序列化好的树解序列化。
题目是比较宽泛的，对于序列化返回是否是str无要求，序列化返回最后有没有None也没有要求。
思路：
序列化：
通过层序遍历，假想是一颗满二叉树，如果是叶子节点的话就将叶子的左右孩子设置为None,然后当节点为None,退出遍历。
队列q保存两种节点，一种是真实节点，一种是None,如果是None弹出，则将None添加到res中,如果非None弹出，则val添加到res,并将左右孩子入队，如果没有左右孩子，则将None入队
解序列化：
首先遍历一遍列表将除根节点外所有节点值实例化节点类并保存于队列中，然后用一个临时list stack保存每层的节点,一层一层处理stack里的node.将队列弹出来的node,作为当前stack里的孩子，并将其保存到下一轮的父亲stack中，处理个数为stack里保存的node个数为：1， 2， 4， 8...
```

```
题目：
[1,2,3,null,null,4,5]
 序列化结果：
 [1,2,3,null,null,4,5,null,null,null,null]
 依然正确
```

> 同层序遍历，同题目意思。


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #层序遍历，迭代方式，假设树为满二叉树，如果节点没有左右子树，将左右子树认为是None添加到层序遍历的结果中
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)
        #队列q保存两种节点，一种是真实节点，一种是None,如果是None弹出，则将None添加到res中,如果非None弹出，则val添加到res,并将左右孩子入队，如果没有左右孩子，则将None入队
        while q:
            x = q.popleft()
            if x == None:
                res.append(None)
            else:
                res.append(x.val)
                if x.left:
                    q.append(x.left)
                else:
                    q.append(None)
                if x.right:
                    q.append(x.right)
                else:
                    q.append(None)
        '''           
        while res[-1] == None:
            res.pop()
        '''
        return res
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if not data:
            return None
        #先建好node节点，并保存在队列里
        nodes = deque()
        root = TreeNode(data[0])
        for i in range(1, len(data)):
            if data[i] is None:
                node = None
            else:
                node = TreeNode(data[i])
            nodes.append(node)
        #print(nodes)
        stack = [root]
        
        #一次处理一层，将某层的节点保存在栈里，然后将队列里的节点弹出，插入到此时栈里的节点的左右孩子上。
        while nodes:
            new_stack = []
            for father in stack:
                if father:
                    left_child, right_child = nodes.popleft(), nodes.popleft()
                    if left_child:
                        father.left = left_child
                    if right_child:
                        father.right = right_child
                    new_stack.append(left_child)
                    new_stack.append(right_child)
            stack = new_stack
        return root
            
            
            
            
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

