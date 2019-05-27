# 53，最大子序和 
** 难度:   **
## 题目

> 原题链接
* https://leetcode-cn.com/problems/maximum-subarray/

> 内容描述

```
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
```
> example 1 
```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

```



## 解题方案
``` 
动态规划法，虽然我还不太懂，
状态方程

f(i)=max(f(i-1)+a[i],a[i])

```


> 我的解答

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #max_sum = max(max_sum, i)
        res = max_sum = -9999999999999999999999999999999
        for i in nums:
            max_sum = max(max_sum + i, i)
            res = max(res, max_sum)
        return res
                

```
