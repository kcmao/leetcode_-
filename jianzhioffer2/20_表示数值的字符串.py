# -*- coding: utf-8 -*-
"""
A[.[B]][e|EC] or .B[e|EC]
"""
def isNumeric(string):

    if string is None or len(string) == 0:
        return False
    #A
    index , numeric = isInteger(string, 0)


    if index < len(string):
        #.
        if string[index] == ".":
            index += 1
            #B
            index, numeric = isUnsignedInteger(string, index)


        if index < len(string):
            #E/e
            if string[index] == "e" or string[index] == "E":
                index += 1
                #c
                index, new_numeric = isInteger(string, index)

            numeric = numeric and (len(string) == index) and new_numeric

    return numeric

def isInteger(string, index):

    if index < len(string) and (string[index] == "+" or string[index] == "-"):
        index += 1

    tmp_index = index
    while index < len(string) and string[index].isdigit():
        index += 1
    return index, index > tmp_index

def isUnsignedInteger(string, index):
    tmp_index = index
    while index < len(string) and string[index].isdigit():
        index += 1
    return index, index > tmp_index



def Test(testname, string, expected):
    if isNumeric(string) == expected:
        print(testname, "Passed")
    else:
        print(testname, "Failed")


if __name__ == "__main__":
    Test("Test1", "100", True)
    Test("Test2", "123.45e+6", True)
    Test("Test3", "+500", True)
    Test("Test4", "5e2", True)
    Test("Test5", "3.1416", True)
    Test("Test6", "600.", True)
    Test("Test7", "-.123", True)
    Test("Test8", "-1E-16", True)
    Test("Test9", "1.79769313486232E+308", True)

    print("\n")

    Test("Test10", "12e", False)
    Test("Test11", "1a3.14", False)
    Test("Test12", "1+23", False)
    Test("Test13", "1.2.3", False)
    Test("Test14", "+-5", False)
    Test("Test15", "12e+5.4", False)
    Test("Test16", ".", False)
    Test("Test17", ".e1", False)
    Test("Test18", "e1", False)
    Test("Test19", "+.", False)
    Test("Test20", "", False)


