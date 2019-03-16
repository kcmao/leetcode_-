# 151，翻转字符串里的单词
**<font color=red>难度: 中等</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/reverse-words-in-a-string/

> 内容描述

```
给定一个字符串，逐个翻转字符串中的每个单词。

输入: "the sky is blue",
输出: "blue is sky the".

说明:

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
进阶: 请选用C语言的用户尝试使用 O(1) 空间复杂度的原地解法。
```
## 解题方案
```
python等于作弊
```

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_li = s.split()
        return ' '.join(s_li[::-1])
``` 
 