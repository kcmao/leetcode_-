# 0189 
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/rotate-array/

> 内容描述

```
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。。
```
> example 1 
```
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
```
> example 2
```
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
```
> 说明
```
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
```
## 解题方案
```
设置 0 1 2 3为四个方向，设置 left\right\right\down为四个最大边界，如：for i in range(left, right+1 ) 通过 for循环遍历某个方向上的所有值，其中left, right+1为边界.

注意细节：
先拿k取余nums的长度，这样如果是len = 2 ，k = 3 ，实际上就等于移动一次，等于k =1,节省时间，然后就是取出后k个数字暂存，然后nums向后移动k,然后再把k付给nums前k个。
```
> 48 ms beats 99%
```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
           
        l = len(nums)
        k = k % l
        if k != 0:
            tmp = nums[-k:]
            #for i in range(l - 1, k-1, -1)
                #nums[i] = nums[i-k]这种写法更好。
            for i in range(l-k):
                nums[l-i-1] = nums[l-1-i-k]
            nums[:k] = tmp 

        
        '''
        #超出时间限制
        l = len(nums)
        for steps in range(k):
            tmp = nums[-1]
            for i in range(l):
                nums[l-i-1] = nums[l-i-2]
            nums[0] = tmp
        '''
``` 
