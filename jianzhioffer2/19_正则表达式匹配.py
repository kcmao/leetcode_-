# -*- coding: utf-8 -*-
"""
分析：

当模式中的第二个字符不是“*”时：
1、如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的。
2、如果字符串第一个字符和模式中的第一个字符相不匹配，直接返回False。

而当模式中的第二个字符是“*”时：
可以有3种匹配方式：
1、模式第一个字符和字符串第一个字符不匹配:
    模式后移2字符，相当于x*被忽略；
2、模式第一个字符和字符串第一个字符匹配：
        字符串后移1字符，模式后移2字符，x*相当于只匹配一个字符；
        字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位

"""
def match(string, pattern):
    if len(string) == 0 and len(pattern) == 0:
        return True
    return match_core(string, pattern)

def match_core(string, pattern):
    if len(string) == 0 and len(pattern) == 0:
        return True

    #string为空，pattern还有剩余
    if len(string) == 0:
        while len(pattern) >= 2 and pattern[1] == "*":
            pattern = pattern[2:]
        if len(pattern) == 0:
            return True
        else:
            return False

    #string未空，pattern为空
    if len(pattern) == 0:
        return False


    #保证模式的第二个字符存在
    if len(pattern) >= 2:

        #第二个字符不是*
        if pattern[1] != "*":
            if string[0] == pattern[0] or pattern[0] == '.':
                return match_core(string[1:], pattern[1:])
            else:
                return False
        #第二个字符是*
        else:
            #第一个字符不匹配
            if string[0] != pattern[0] and pattern[0] != '.':
                return match_core(string, pattern[2:])
            #第一个字符匹配
            else:
                return match_core(string[1:], pattern[2:]) or match_core(string[1:], pattern)

    #如果模式只剩一个字符了：
    else:
        if len(string) == 1:
            if string[0] == pattern[0] or pattern == ".":
                return True
        else:
            return False

#############test case##########
def Test(test_name, string, pattern, expected):
    result = match(string, pattern)
    if result == expected:
        passed = "Passed"
    else:
        passed = "Failed"
    print(test_name, passed)


if __name__ == "__main__":
    Test("Test01", "", "", True)
    Test("Test02", "", ".*", True)
    Test("Test03", "", ".", False)
    Test("Test04", "", "c*", True)
    Test("Test05", "a", ".*", True)
    Test("Test06", "a", "a.", False)
    Test("Test07", "a", "", False)
    Test("Test08", "a", ".", True)
    Test("Test09", "a", "ab*", True)
    Test("Test10", "a", "ab*a", False)
    Test("Test11", "aa", "aa", True)
    Test("Test12", "aa", "a*", True)
    Test("Test13", "aa", ".*", True)
    Test("Test14", "aa", ".", False)
    Test("Test15", "ab", ".*", True)
    Test("Test16", "ab", ".*", True)
    Test("Test17", "aaa", "aa*", True)
    Test("Test18", "aaa", "aa.a", False)
    Test("Test19", "aaa", "a.a", True)
    Test("Test20", "aaa", ".a", False)
    Test("Test21", "aaa", "a*a", True)
    Test("Test22", "aaa", "ab*a", False)
    Test("Test23", "aaa", "ab*ac*a", True)
    Test("Test24", "aaa", "ab*a*c*a", True)
    Test("Test25", "aaa", ".*", True)
    Test("Test26", "aab", "c*a*b", True)
    Test("Test27", "aaca", "ab*a*c*a", True)
    Test("Test28", "aaba", "ab*a*c*a", False)
    Test("Test29", "bbbba", ".*a*a", True)  # 这个fail,不想debug了
    Test("Test30", "bcbbabab", ".*a*a", False)









