# 118.  杨辉三角
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/pascals-triangle/solution/

> 内容描述

```
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。
```
> example 1 
```
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```


## 解题方案
```
如果能够知道一行杨辉三角，我们就可以根据每对相邻的值轻松地计算出它的下一行
注意：
首先，我们会生成整个 triangle 列表，三角形的每一行都以子列表的形式存储。然后，我们会检查行数为 00 的特殊情况，否则我们会返回 [1][1]。如果 numRows > 0numRows>0，那么我们用 [1][1] 作为第一行来初始化。
注意遍历的时候行数和列数是多少。官方解答比我的好多了。 
```
> 官方解答
```python
class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
``` 
> 我的解答
* beats 93.41%
```python
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1],[1,1]]
        tmp = []
        #假设之前的是res[i]
        for i in range(1, numRows-1): #外共循环共循环numRows - 2行
            print(i)
            next_row = [1] #每行第一个为1
            for j in range(0, i):
                print('j',j)
                tmp = res[i][j] + res[i][j+1]
                #print(tmp)
                next_row.append(tmp)
            next_row.append(1) #最后一个为1
            res.append(next_row)
        return res
```

## 复杂度分析
```
时间复杂度：O(numRows^2)

很明显外层循环需要运行 numRows次，但在外层循环的每次迭代中，内层 循环要运行 rowNum 次。因此，triangle 发生的更新总数为 1 + 2 + 3 ... + numRows
空间复杂度：同时间复杂度
```
