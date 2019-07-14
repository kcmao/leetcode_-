一定要看这篇快排的简书
https://www.jianshu.com/p/2b2f1f79984e

伪快排的快排代码,简洁版快排，浪费存储空间
# 1
```python
def quick_sort0(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        more_than_pivot = [x for x in array[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)

#print(quick_sort([3,4,6,1,2,8]))
#一行实现：
#quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
    
```
# 2
```python

def quick_sort1(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort1(array1, low, left - 1)

```

# 3
用Python写一个C风格的快排(这里可以体会到快排的精髓)

```python
# 最上层的封装
def quick_sort2(L):
    return q_sort(L, 0, len(L)-1)

# 真正的快排
def q_sort(L, left, right):
    #判断条件为 left 小于 right
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot-1)
        q_sort(pivot+1, right)
    return L

# 分割程序，返回的
```


这个函数的核心是pivot = Partition(L, left, right)，
在执行它之前，列表的值为[5, 9, 1, 11, 6, 7, 2, 4]，而Partition函数做的事情是找到一个分组标准，然后进行分组，让它左边的值比它小，右边的值比它大。
在经过Partition函数分组后，列表变为[4, 2, 1, 5, 6, 7, 11, 9]，
并把5的下标值(也就是3)返回给pivot，此时列表变成两个小列表[4, 2, 1]和[5, 6, 7, 11, 9] ，
 之后调用q_sort，就是调用q_sort(L,0, 2)和q_sort(L, 4 ,7)，对其进行Partition操作，直到整个列表有序为止

```python
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
    #返回的是5的下标值，此时left = right，即为pivotkey的真实下标
    return left
```
