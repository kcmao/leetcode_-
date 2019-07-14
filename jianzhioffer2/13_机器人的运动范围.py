# -*- coding: utf-8 -*-
"""
// 面试题13：机器人的运动范围
// 题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它
// 每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
// 大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。
// 但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
"""

def find_path_in_matrix(rows, cols, threshold):
    #边界1
    if rows < 0 or cols < 0:
        return
    #边界2
    if threshold < 0:
        return


    large_length = find_path_core(x=0, y=0, threshold=threshold, rows=rows, cols=cols)
    return large_length



def find_path_core(x, y, threshold, rows, cols):
    """
    递归回溯
    :param x: x
    :param y: y
    :param matrix:
    :param threshold:
    :param rows:
    :param cols:
    :param length
    :return: length
    """
    count = 0

    if check_digits(x, y, rows, cols,threshold):
        count = 1 + max(find_path_core(x+1, y, threshold, rows, cols),
                    find_path_core(x, y+1, threshold, rows, cols))

    return count




def check_digits(x, y, rows, cols, threshold):

    if x < 0 or y < 0 or x > rows or y > cols:
        return False
    x = str(x)
    y = str(y)
    digits_sum = 0
    for n in x:
        digits_sum += int(n)
    for n in y:
        digits_sum += int(n)

    if digits_sum > threshold:
        return False
    else:
        return True

#错的，因为中间有不满足，然后后面格子满足的，而机器
def find_path_in_matrix2(rows, cols, threshold):
    count = 0
    for i in range(rows):
        for j in range(cols):
            if check_digits(i, j, rows, cols, threshold):
                count += 1
    return count


#############################testing##############################3
def test(testname, threshold, rows, cols, expected):
    length = find_path_in_matrix2(rows, cols, threshold)
    if length == expected:
        result = "PASS"
    else:
        result = "FAILED"
    print(testname+":  ", length, "  ", expected,"   ",  result)

def test_case():
    test("test1", 5 ,10, 10, 21)
    test("test2", 15, 20, 20, 359)
    test("test3", 10, 1, 100, 29)
    test("test4", 10, 1, 10, 10)
    test("test5", 15, 100, 1, 79)
    test("test6", 15, 10, 1, 10)
    test("test7", 15, 1, 1, 1)
    test("test8", 0, 1, 1, 1)
    test("test9", -10, 10, 10, 0)



if __name__ == "__main__":
    #print(check_digits(35, 38))
    test_case()

