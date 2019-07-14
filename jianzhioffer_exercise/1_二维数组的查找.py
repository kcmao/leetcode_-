# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:39:25 2019
 
@author: mkc
"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here\
        i = 0
        j = len(array) - 1
        if not array or not array[0]:
            return False
            
        #从右上角开始找，两种情况，同时要注意要判断下标是否越界        
        while True:
            if target > array[i][j]:
                i += 1
            if i >= len(array):
                return False      
            if target < array[i][j]:
                j -= 1
            if j < 0:
                return False
            if target == array[i][j]:
                return True
        
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
So = Solution()
re = So.Find(8, array)
print(re)
