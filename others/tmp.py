# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 17:57:22 2018

@author: mkc
"""
def quick_sort1(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        more_than_pivot = [x for x in array[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)
print(quick_sort([3,4,6,1,2,8]))


def quick_sort2(L):
    return q_sort(L, 0, len(L)-1)


def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot-1)
        q_sort(L, pivot+1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]
    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]
    
    L[left] = pivotkey
    return left

L = [5, 9, 1, 11, 6, 7, 2, 4]
print(quick_sort2(L))