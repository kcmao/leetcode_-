# -*- coding: utf-8 -*-
"""
题目：实现函数Power(base, exponent), 求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
"""
def Power(base, exponent):
    """

    :param base:
    :param exponent:
    :return:
    """
    """
    1, exponent > 0
    2, exponent == 0
    3, exponent < 0
        (0, -10) :如果base = 0, exponent<0,则出现给0取倒数，会出错
    """

    if base == 0:
        return 0

    if exponent == 0:
        return 1
    multiply = 1
    if exponent < 0:
        exponent = -exponent
        while exponent :
            multiply = multiply * base
            exponent -= 1
        return 1 / multiply

    while exponent:
        multiply = multiply * base
        exponent -= 1
    return multiply

if __name__ == "__main__":
    print(Power(1, 3))