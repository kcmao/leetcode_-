# 014. 最长公共前缀  
**<font color=red>难度: 简单</font>**
## 题目

> 原题链接
* https://leetcode-cn.com/problems/longest-common-prefix/

> 内容描述

```
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
```
> example 1 
```
输入: ["flower","flow","flight"]
输出: "fl"
```
> example 2
```
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
```



## 解题方案
* 复杂度 
``` 
我的解题方案：找到list中最小的字符串，假设长度为n，外循环控制长度为n，i控制长度,内循环遍历strs list的每一个字符串，如果大家开头的前i个字母都一样，i++，否则直接返回前i个字母。
```
## 测试用例的特例注意
```
1. []
2. ['']
3. ['a']
```

> 我的解答
* beats 2%
```python
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or '' in strs:   #[]、['']测试用例通不过。
            return ""
        short_str = min(strs, key=len)
        i = 0
        while i < len(short_str):   
            for j in range(len(strs)):
                if strs[j][i] == short_str[i]:
                    continue
                return short_str[:i]
            i += 1
        return short_str     #一定注意这个short_str的return,否则测试用例 ['a'] 通不过。
```

## 参考解法 
```
其实和我的解法一样，但是没有了那句话，求min(),可能这个比较耽误时间。

以一个小例子来解释，strs=['laa', 'lab', 'lac'], 如果存在LCP的话它肯定就在第一个字符串strs[0]中，并且LCP的长度肯定不会大于strs[0]的长度

依次假设LCP长度为0到len(strs[0]),在每一轮循环中:  
只要strs中存在比当前长度i更短的string，立刻返回上一轮LCP，即strs[0][:i]
只要strs中存在当前index字符与LCP该index不相同的字符串，立刻返回上一轮LCP，即strs[0][:i]
如果一直没返回，说明strs[0]本身就是LCP，返回它
```

