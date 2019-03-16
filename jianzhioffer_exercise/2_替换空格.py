# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:19:46 2019

@author: mkc
"""
"""
申明一个列表，遍历整个字符串，将字符放到list中，
遇到空格就将“%20”放入字符串中，
"""
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s_li = []
        for i in s:
            if i == " ":
                s_li.append("%20")
            else:
                s_li.append(i)
        #将列表元素连起来
        return "".join(s_li)
    
s1 = "We are Happy"
s2 = " We don't Happy"

so = Solution()
re = so.replaceSpace(s2)
print(re)
