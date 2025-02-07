# 1. Two Sum 两数之和
**<font color=red>难度: Easy</font>**
## 刷题内容

> 原题链接
* https://leetcode.com/problems/two-sum
* https://leetcode-cn.com/problems/two-sum/description

> 内容描述

```
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```
## 解题方案
* 可参考https://github.com/apachecn/awesome-algorithm/blame/d2f578782330e402e7eaa2a5778cee3d655e4a1a/docs/Leetcode_Solutions/Python/001._two_sum.md
>1 暴力遍历 
通过两轮遍历求解  
时间复杂度: O(N^2) 空间复杂度: O(1) 
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_i,i in enumerate(nums):
            for index_j,j in enumerate(nums[index_i+1:]):
                if i + j == target:
                    return [index_i,index_j+index_i+1]
``` 
>2 通过字典 
 牺牲空间换取时间，建立字典num_maps存放差值和需要的索引    
 时间复杂度: O(N) 空间复杂度: O(N) 
```
          2    7    11    15   target = 9
num_maps {7:0, 2:1, -2:2,-6:3}
遍历字典的key，如果nums中有值和key一样，直接返回key对应的value.
``` 
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for index, num in enumerate(nums):
            a = target - num
            if num in num_map:
                return [num_map[num], index]
            else:
                num_map[a] = index
```     
