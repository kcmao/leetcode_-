# 0119 Pascal's Triangle II
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/pascals-triangle-ii/

> 内容描述

```
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
```
> example 1 
```
输入: 3
输出: [1,3,3,1]
```

> 进阶
```
你可以优化你的算法到 O(k) 空间复杂度吗？

```
## 解题方案
```
设置tmp保存i行的结果，ret为第i-1行，然后再将tmp赋给i行。
这个思路可以让空间复杂度降低很多。
```
> 48 ms beats 99%
```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
    
        if rowIndex == 0:
            return [1]
        for i in range(1, rowIndex+1):
            tmp = [1]
            for j in range(1, i):
                tmp.append(ret[j-1]+ret[j])
            tmp.append(1)
            ret = tmp
        return ret
``` 
