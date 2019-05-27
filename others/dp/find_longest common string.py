# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:38:17 2018

@author: kmao
"""
"""
动态规划法，建立一个表查看斜对角线的长度。
详见如下：
https://segmentfault.com/a/1190000007963594
输入：str1,str2
返回：最长的子串和子串长度
"""
'''
mlen = 0
p = 0
table = np.zeros((len(str1)+1, len(str2)+1))
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            table[i+1, j+1] = table[i, j] + 1
            if table[i+1, j+1] >=mlen:
                mlen = table[i+1,j+1]
                p = i + 1
print(mlen)
print(str1[int(p-mlen):p])
'''  


import numpy as np
def find_longest_commen_string(str1, str2):
    mlen = 0
    p = 0
    table = np.zeros((len(str1)+1, len(str2)+1))    #建立一张宽高为str1,str2长度+1的表，方便后面计算累加和
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                table[i+1, j+1] = table[i, j] + 1
                if table[i+1, j+1] >=mlen:
                    mlen = table[i+1,j+1]
                    p = i + 1
    longest_str = str1[int(p-mlen):p]
    print("the longest length is:", mlen)
    print("the longest str is:", longest_str)
    return mlen, longest_str
    
    
 
    
    
str1 = 'abcdefghixyrf'
str2 = 'xyzabcdeghdeab'   
find_longest_commen_string(str1, str2)

          