# -*- coding:utf-8 -*-

'''
用快排的partition,对数组排序，找到前k个数的位置，然后再用冒泡找到前k个。
'''



class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def partition(tinput, left, right):
            tmp = tinput[left]
            while left < right:
                while left < right and tinput[right] > tmp:
                    right -= 1
                if(left < right):
                    tinput[left] = tinput[right]
                    left += 1
                
                while left < right and tinput[left] <= tmp:
                    left += 1
                if(left < right):
                    tinput[right] = tinput[left]
                    right -= 1
                
            tinput[right] = tmp
            return left

        if len(tinput) < k:
            return []

        right = len(tinput) - 1
        pos = -1
        while pos + 1 < k:
            pos = partition(tinput, pos + 1, right)

        for i in range(0, pos):
            for j in range(i, pos):
                if tinput[i] > tinput[j]:
                    t = tinput[i]
                    tinput[i] = tinput[j]
                    tinput[j] = t
        return tinput[:k]

if __name__ == "__main__":
    s = Solution()
    k_li = s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],1)
    print(k_li)