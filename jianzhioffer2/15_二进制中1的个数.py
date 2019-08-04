# -*- coding: utf-8 -*-
"""
// 面试题15：二进制中1的个数
// 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如
// 把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。
"""
"""
1：一个整数如何转化成二进制数
2：二进制数怎么统计1的个数
3：负数怎么办
    对与c不用关心
    对于python ,将其&0XFFFFFF
4: 
"""

def numberOf1(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n != 0:
        count += 1
        n = n & (n - 1)
    return count

if __name__ == "__main__":
    print(numberOf1(3))