# 066. Plus one 加一
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/plus-one/

> 内容描述

```
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
```
> example 1 
```
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
```
> example 2
```
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
```

## 解题方案
```
对于python很简单，主要用现成的int()和str()函数，注意细节即可。
```

```python
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        for i in digits:
            s += str(i)
        n_1 = int(s)
        n_2 = str(n_1 + 1)
        l = []
        for i in n_2:
            l.append(int(i))
        return l
``` 
