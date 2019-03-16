# 747. 至少是其他数字两倍的最大数  
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/

> 内容描述

```
在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。
```
> example 1 
```
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
```
> example 2
```
输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.
```


## 解题方案
``` 
很简单，先找出最大值，保存为a，接着一轮遍历，直接判断是否有乘以2大于a的数，如果有，直接停止，没有则返回a的索引，遍历的同时注意判断排除a.


```

> 我的解答
* beats 78.69%
```python
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = max(nums)
        for i,element in enumerate(nums):
            if element == a:
                pass
            elif 2 * element > a:
                return -1
        return nums.index(a)  #返回a的索引        
```