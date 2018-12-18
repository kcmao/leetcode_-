# 167. 两数之和  
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

> 内容描述

```

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```



## 解题方案
``` 
注：参考了别人的
最小的min加最大的max  = tar，如果小就增加min，大就减小max，然后无限逼近target

```

> 我的解答

```python
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #二分法加双指针
        i = 0
        j = len(numbers) - 1
        while i < j: 
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1      
```