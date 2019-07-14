# -*- coding: utf-8 -*-
"""
// 面试题3（一）：找出数组中重复的数字
// 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
// 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，
// 那么对应的输出是重复的数字2或者3。
"""

def duplicate(array):
    """
    使用python的字典作为hash
    :param array:
    :return: (true/false, number )
    """
    if array is None:
        return False, None
    array_dict = {}
    for a in array:
        if a in array_dict:
            return True, a
        else:
            array_dict[a] = 0
    return False, None

def duplicate2(array):
    """
    使用数组作为hash
    :param array:
    :return:
    """
    if array is None:
        return  False, None
    array_dict = [-1 for i in range(len(array))]
    for i in array:
        if array_dict[i] > -1:
            return True, i
        else:
            array_dict[i] += 1
    return False, None





if __name__ == "__main__":
    array1 = [4, 3, 1, 2, 5, 3, 0]
    array2 = [2, 1, 0]

    result1 = duplicate(array1)
    print(result1)

    result2 = duplicate(array2)
    print(result2)

    result1 = duplicate2(array1)
    print(result1)

    result2 = duplicate2(array2)
    print(result2)


