# 498. 对角线遍历  
**<font color=red>难度: 中等</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/diagonal-traverse/

> 内容描述

```
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
```
> example 1 
```
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]
```


## 解题方案
* 参考了https://www.jianshu.com/p/2cfe7c69e3eb
``` 
关键是找出规律
分析一下遍历顺序的特点，可以看出，对角线的方向跟索引和（行的索引值+列的索引值）的奇偶性有关，然后加上边界情况，遍历的路线大概就出来了。
具体可以分为以下几种情况：

索引和为偶数：
元素在第一行，往右走
元素在最后一列，往下走
其他情况，往右上走

索引和为奇数：
元素在第一列，往下走
元素在最后一行，往右走
其他情况，往左下走

```


> 我的解答
```python
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #解法复制了https://www.jianshu.com/p/2cfe7c69e3eb
        hight = len(matrix) #m行
        if hight == 0:
            return matrix
        witdh = len(matrix[0]) #n列  
        result = []
        r = 0                     #行索引
        c = 0                     #列索引
        for i in range(hight * witdh):
            result.append(matrix[r][c])
            if (r+c)%2  == 0:  
                if c == witdh - 1: #最后一列，注意一定是先判断最后一列再判断是否使第一行
                    r += 1
                elif r == 0 :  #第一行
                    c += 1
                else:          #其他
                    r -= 1
                    c += 1
            else:
                if r == hight - 1:  #最后一行，注意一定是先判断最后一行再判断是否使第一列
                    c += 1
                elif c == 0:        #第一列
                    r += 1
                else:               #其他
                    c -= 1
                    r += 1
        return result                
```
