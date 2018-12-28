# 054. 螺旋矩阵
**<font color=red>难度: 中等</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/spiral-matrix/

> 内容描述

```
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
```
> example 1 
```
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
```
> example 2
```
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## 解题方案
```
设置 0 1 2 3为四个方向，设置 left\right\right\down为四个最大边界，如：for i in range(left, right+1 ) 通过 for循环遍历某个方向上的所有值，其中left, right+1为边界.

注意细节：
1.注意有的加1的问题。如for i in range(left, right+1 )
2.注意用direction去作为判断值进入，这样可以做到不用四个方向都走完才进入if，
3.反转可以用reversed()函数
```

```python
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        left = 0
        up = 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1
        res = []
        #direction 控制方向 0 -> 右, 1 ->下, 2 -> 左, 3 -> 上 
        
        direction = 0
        while True:
            if direction == 0:
                for i in range(left, right+1 ):
                    res.append(matrix[up][i])
                up += 1
            elif direction == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in reversed(range(left, right+1)):
                    res.append(matrix[down][i])
                down -= 1
            else:
                for i in reversed(range(up, down+1)):
                    res.append(matrix[i][left])
                left += 1
            if left > right or up > down:
                return res
            direction = (direction + 1) % 4
``` 
