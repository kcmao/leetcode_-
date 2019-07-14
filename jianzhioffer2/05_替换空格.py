# -*- coding: utf-8 -*-

"""
// 面试题5：替换空格
// 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
// 则输出“We%20are%20happy.”。
"""

"""
O(n2):从头到尾扫描字符串，碰到空格就替换，每替换一次，就要将后面的字符往前移一步
O(n):两根指针，从后往前替换。
"""
"""
1，计算新的数组长度：新=原来的数组长度+空格数*2
2，首先准备两根指针，p1和p2,
    p1指向字符串的末尾，
    p2指向替换之后的字符串的末尾，
    然后向前移动
"""

def replace_space(string):
    """

    :param string: [string]
    :return:
    """
    string_li = []
    for s in string:
        if s == " ":
            string_li.append("%20")
        else:
            string_li.append(s)

    return "".join(string_li)


if __name__ == "__main__":
    print(replace_space("we are friend"))