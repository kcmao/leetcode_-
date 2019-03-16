# 028. 实现strStr()  
**<font color=red>难度: 简单</font>**
## 题目

> 原题链接
* https://leetcode-cn.com/problems/implement-strstr/

> 内容描述

```
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。。
```
> example 1 
```
输入: haystack = "hello", needle = "ll"
输出: 2
```
> example 2
```
输入: haystack = "aaaaa", needle = "bba"
输出: -1
```
> 说明
```
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
```


## 解题方案
* 思路 1 时间复杂度: O(m * n) 空间复杂度: O(1)******
``` 
暴力匹配，外循环执行len(haystack)-len(needle)+1次（m-n+1）内循环执行n次，用来判断是否匹配。
```

> 我的解答
* beats 71%
```python
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        if not needle or n == 0:    #保证needle不是0、''、None
            return 0
        for i in range(len(haystack)-len(needle)+1): #注意遍历次数
            if haystack[i] == needle[0]:
                j = 1
                while j < n and haystack[i+j] == needle[j]: #用while不用for,用j作计数器
                    j += 1
                if j == n:
                    return i
        return -1      
```
> 参考，作弊方法
```
作弊，python str.find() 底层实现是 Boyer–Moore–Horspool 算法

The time complexity is O(N) on average, O(NM) worst case (N being the length of the longer string, M, the shorter string you search for).
```
```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
```