# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:39:41 2018

@author: kmao
"""
#最好理解了
def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if alist[i] > alist[j]:
                    alist[i], alist[j] = alist[j], alist[i]
    return alist



#？？？我没搞懂（程序也可能有问题）
def quick_sort(alist, first, last):
    #递归退出条件
    if first >= last:
        return alist
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        #high 左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] <= mid_value:
            low += 1
        alist[high] = alist[low]
    #循环退出时，low == high
    alist[low] = mid_value
    #对low左边列表执行快速排序
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


def quick_sort2( )
        
        
            

def insert_sort(alist):
    def insert_value(array, value):
        for i, existing in enumerate(array):
            if existing > value:
                array.insert(i, value)
                return
        array.append(value)        
    result = []
    for value in alist:
        print(result)
        insert_value(result, value)
    return result





#比较n+(n-1)+(n-2)...+1 = n(n-1)/2次
#比较次数固定，和输入数据无关
#每迭代一轮，选择一个最小的放到前面。
#外层循环每次从数列第i个起找到一个最小的放到第i个位置上，内层循环负责找最小值。（前i个已经排好序）
def select_sort(alist):
    for i in range(len(alist) -1):
        min_index = i                                     #m用来标记最小值的下标
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist

#c++指针操作的方式
'''
def merge_sort(alist, low, high):
    if high - low < 2:
        return 
    mid = (low + high) / 2
    merge_sort(alist, low, mid)
    merge_sort(alist, mid+1, high)
    merge(alist, low, mid, high)
    
    def merge(alist, low, mid, high):
        i = 0
        j = 0
        lb = mid - low
        lc = high - mid - 1
        while i < lb or j < lc:
            if alist[i]
'''

def merge_sort(alist):
    #写了好久，因为不停报错 
    def merge(a, b):
        res = []
        i = 0
        j = 0
        while i < len(a)  or j < len(b) :
            try:
                if j >= len(b) or a[i] <= b[j]:
                    res.append(a[i])
                    i += 1
            except:
                pass
            try:
                if i >= len(a) or b[j] < a[i]:
                    res.append(b[j])
                    j += 1
            except:
                pass
        return res
    
    low = 0
    high = len(alist) - 1
    mid = (low + high) // 2 + 1
    if len(alist) < 2:
        return alist
    return merge(merge_sort(alist[:mid]), merge_sort(alist[mid:]))
    
    

             
        
        
        

if __name__ == '__main__':
    from random import randint
    import cProfile
    import pstats
    max_size = 10**4
    alist = [randint(0, max_size) for _ in range(max_size)]

    #~~~~~~~~~~~~~~~~~test performance~~~~~~~~~~~~~~~~~~~~~~~~~~~
    test = lambda:merge_sort(alist)
    #test = lambda:bubble_sort(alist)
    profiler = cProfile.Profile()
    profiler.runcall(test)
    
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats() 
    #print(insert_sort(alist))
alist = [4, 2, 5, 7, 1, 6, 9, 3, 8]
#print(bubble_sort(alist))
print(insert_sort(alist))
#print(select_sort(alist))
#print(quick_sort(alist, first = 0, last = len(alist) - 1))

































