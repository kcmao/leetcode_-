# -*- coding: utf-8 -*-
"""
// 面试题15：二进制中1的个数
// 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如
// 把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。
"""
def max_product_after_cuting(n):
    """
    动态规划解法
    时间 O(n^2)，空间O(n)
    """
    """
    总长度为 N，砍了一刀i
    f(n) = f(i)*f(n-i)
        
    """
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    return max_product_after(n)


def max_product_after(n):
    #此处切到2就不切了，所以n= 2，返回2
    if n < 2:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 3

    max_product = 0
    for i in range(1, n):
        product = max_product_after(i) * max_product_after(n-i)
        if product > max_product:
            max_product = product

    return max_product

def max_product_iteration(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    product = [0 for i in range(n+1)]
    product[0] = 0
    product[1] = 1
    product[2] = 2
    product[3] = 3

    for i in range(4, n+1):
        max_product = 0
        for j in range(1, i):
            product_j = product[j] * product[i-j]
            if max_product < product_j:
                max_product = product_j
        product[i] = max_product

    return product[n]


def test(test_name, n, expected):
    #product = max_product_after_cuting(n)
    product = max_product_iteration(n)
    if product == expected:
        result = "PASSED"
    else:
        result = "FAILED"
    print(test_name+":  ", product, "  ", expected, "  ", result)

def test_case():
    test("test1", 1, 0)
    test("test2", 2, 1)
    test("test3", 3, 2)
    test("test4", 4, 4)
    test("test5", 5, 6)
    test("test6", 6, 9)
    test("test7", 7, 12)
    test("test8", 8, 18)
    test("test9", 9, 27)
    test("test10", 10, 36)


if __name__ == "__main__":
    test_case()

