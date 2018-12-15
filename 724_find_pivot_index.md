# 724. 寻找数组的中心索引  
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/find-pivot-index/

> 内容描述

```
给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
```
> example 1 
```
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释: 
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
```
> example 2
```
输入: 
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释: 
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
```


## 解题方案
``` 
将全部数组求和，并计算前i-1项和，i+1到n项和，如果相等，返回i.

```

> 我的解答
* beats 88.48%
```python
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_total = sum(nums)
        sum_to_i = 0
        for i, element in enumerate(nums):
            if i==0:
                sum_to_i = 0 #不能忘了把i=0考虑进去
            else:
                sum_to_i += nums[i-1]
            sum_from_i = sum_total-sum_to_i - element
            if sum_to_i == sum_from_i:
                return i
        return -1               
```
## 复杂度分析
```
通过一次sum()求和，接着一轮遍历即可，遍历过程中计算并保存前i项和。
```