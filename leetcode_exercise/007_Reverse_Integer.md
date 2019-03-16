# 1. Reverse Integer 整数反转 
**难度 easy**
> 原题连接
* https://leetcode.com/problems/two-sum

> 内容描述 

示例1：
```
输入: 123
输出: 321
```
示例 2:
```
输入: -123
输出: -321
```
示例 3:
```
输入: 120
输出: 21
```
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
## 解题方案
> 思路 
```
思路：先将int转成字符串，然后取反，[:-1]为去掉负号，再转换成int,然后判断绝对值是否大于2^31,如果da
``` 

```python
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)[::-1] 
        b = int(a) if x >= 0 else -int(a[:-1]) #判断正负并转回
        if abs(b) > 2**31 - 1:
            return 0
        else:
            return b
```

