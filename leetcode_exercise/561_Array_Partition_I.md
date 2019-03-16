# 344. 反转字符串  
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode.com/problems/array-partition-i/description/

> 内容描述

```
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
```



## 解题方案
``` 
思路 1 ******- 时间复杂度: O(NlgN)******- 空间复杂度: O(1)******

排好序每次取一对中的前一个就行了

例如[1,4,3,2]我们排好序为[1,2,3,4]，然后让我们的pair为[1,2]，[3,4]，这样我们结果就是 1 + 3 = 4，肯定最大


```

> 我的解答
* beats 99%
```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])        
```