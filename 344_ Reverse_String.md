# 344. 反转字符串  
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode.com/problems/reverse-string/

> 内容描述

```
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
```



## 解题方案
``` 
因为python：'str' object does not support item assignment
所以s[i], s[j] = s[j], s[i]报错，所以如果非要用双指针的话，可以转成list.
作弊：一句话 return s[::-1]


```

> 我的解答
* beats 20%
```python
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        '''
        因为python：'str' object does not support item assignment
        所以s[i], s[j] = s[j], s[i]报错，所以如果非要用双指针的话，可以转成list.
        作弊：一句话 return s[::-1]
        '''
        lst = list(s)  #转成list再转回来
        start = 0
        end = len(s) - 1
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
        return ''.join(lst)        
```