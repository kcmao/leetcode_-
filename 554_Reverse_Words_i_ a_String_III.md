# 554. 反转字符产 III 
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

> 内容描述

```
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

Example 1:
输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
```
> 注意
```
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
```


## 解题方案
``` 
用python，没有什么难度。 


```

> 我的解答
* beats 94%   32ms
```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_li = s.split()
        ret = [i[::-1] for i in s_li]
        return ' '.join(ret) 
```