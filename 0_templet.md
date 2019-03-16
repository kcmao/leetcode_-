# 20. 有效的括号 
** 难度:   **
## 题目

> 原题链接
* https://leetcode-cn.com/problems/valid-parentheses/

> 内容描述

```
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
```
> example 1 
```
输入: "()"
输出: true

```
> example 2
```
输入: "()[]{}"
输出: true
```


## 解题方案
``` 
输入: "(]"
输出: false


```

> 我的解答

```python
 class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack = []
        table = {'(':')', '{':'}', '[':']'}
        if len(s) % 2 == 1:
            return False
        if not s:
            return True
        for i in s:
            if i in table.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                if table[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                

```
# 别人的代码
```python
  if len(s) % 2 == 1 or len(s) == 0:#这一步真的机智，我只会想到输入一个的状况。。。
            return False

        d = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for i in s:
            # in stack
            if i in d:
                stack.append(i)
            else:
                if not stack or d[stack.pop()] != i: #将 not stack放在前面，两个false判断语句合二为一
                    return False
        """
        else:
            if stack:
                return False

        return True
        """
        return stack ==[] #以上四条语句可以用这条语句替代，一句话代替上面四句
```