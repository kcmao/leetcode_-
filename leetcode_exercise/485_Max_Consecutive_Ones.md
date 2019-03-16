# 485 最大连续1的个数
**<font color=red>难度: 简单</font>**
## 刷题内容

> 原题链接
* https://leetcode-cn.com/problems/max-consecutive-ones/

> 内容描述

```
给定一个二进制数组， 计算其中最大连续1的个数。
```
> example 1 
```
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
```
> 注意
```
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
```


## 解题方案
``` 
一轮遍历，用cnt计数，遇到1 cnt++，遇到0，将cnt重置为0，并随时判断cnt是否为最大，如果max<cnt，将cnt复制给max.

```

> 我的解答
* beats 57%
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        max_cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
                #max_cnt = min(max_cnt, cnt) 同样效果
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0
        return max_cnt       
```