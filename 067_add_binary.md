# 067. 二进制求和  
**<font color=red>难度: 简单</font>**
## 题目

> 原题链接
* https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/

> 内容描述

```
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。
```
> example 1 
```
输入: a = "11", b = "1"
输出: "100"
```
> example 2
```
输入: a = "1010", b = "1011"
输出: "10101"
```


## 解题方案
``` 
主要看了别人代码，用了python,就发现很简单，其实自己写的话并没有那么简单。
int(str, 2):将二进制字符串转换成10进制整型 
bin(int) :将十进制数转换为二进制数
```

> 我的解答
* beats 99.7%
```python
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''
        int(str, 2):将二进制字符串转换成10进制整型 
        bin(int) :将十进制数转换为二进制数
        '''
        return bin(int(a, 2) + int(b, 2))[2:]       
```