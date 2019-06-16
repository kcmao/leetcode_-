"""
用字典记录下出现的数，及出现的次数，这样就很好办了
"""


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if not numbers:
            return 0
        ret = dict()
        tmp = [0, 0]
        if len(numbers) == 1:
            return numbers[0]

        for i in numbers:
            if i in ret:
                ret[i] += 1
                if ret[i] > tmp[1]:
                    tmp[0] = i
                    tmp[1] = ret[i]
            else:
                ret[i] = 1
        if tmp[1] > len(numbers)/ 2:
            return tmp[0]
        else:
            return 0
        
        #for i in ret.keys():
            