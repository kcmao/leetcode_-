# 283. 移动零  
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/move-zeroes/

> 内容描述

```
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

Example 1:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```
> 说明
```
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
```


## 解题方案
``` 
方法很多，我都是抄的。详见：
https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/283._move_zeroes.md

nums.sort()方法, key为lambda函数。

其他方法是双指针方式，我没仔细看，所以没细究。
```

> 我的解答
* beats 20%  
```python
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while 0 in nums:
            nums.remove(0)
            i += 1
        nums.extend([0]*i)
```

> 解答2
```python
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key = lambda x: 1 if x == 0 else 0)

```