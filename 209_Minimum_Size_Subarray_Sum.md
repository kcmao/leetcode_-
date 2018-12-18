# 209. 长度最小的子数组  
**<font color=red>难度: 中等</font>**
## 刷题内容

> 原题链接
* https://leetcode.com/problems/minimum-size-subarray-sum/description/

> 内容描述

```
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
```

> Example 1:
```
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
```
> 进阶
```
如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
```


## 解题方案
``` 
双指针，l和r,while r< len(num)决定了只有一轮遍历，所以复杂度为log(n),r指针往后走，如果sums >= s，l++，往前走一个，同时sums把nums[l]减掉，然后min_len = min(min_len, r-l)随时保存最小的min_len。
自己写的话一定注意各种特列的测试用例，比如：
s = 5, nums = [1,2,1,1] : min_len = 4
s = 5, nums = [0,1]: min_len = 0

```

> 我的解答
* beats 93%
```python
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        sums = 0
        min_len = len(nums)+1 #先假设最小长度为 len(nums)+1，
        while r < len(nums):
            sums += nums[r]
            r += 1
            #print(sums)
            while sums >= s:
                min_len = min(min_len, r-l)
                sums -= nums[l]
                l += 1        
        return min_len if min_len != len(nums)+1 else 0       
```