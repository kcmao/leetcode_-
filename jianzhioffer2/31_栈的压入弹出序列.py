# -*- coding:utf-8 -*-

"""
感想：这题看了剑指offer的答案，知道用辅助栈去解决，但是就是写不出来代码
     感到很难过，自己编程太烂了，烂透了。
     没办法架构出整个流程
     如何设置循环，如何设置退出条件，如何设置对比，

     popV:弹出序列
     push:弹入序列
     stack:辅助栈

     三个序列都是要弹出的

     以popV是否弹完作为判断条件，里面用三个判断：
        1.辅助栈顶与弹出序列第一个数字相同：两者都弹出去
        2.辅助栈顶与弹出序列第一个数字不同，pushV往辅助栈压栈。
        3.当pushV都压完了，弹出序列和辅助栈顶还不一样，那直接false

     退出循环条件：
     当popV都弹完了，说明压栈与出栈是匹配的。

"""



class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV is None or popV is None:
            return False

        if len(pushV) != len(popV):
            return False

        stack = [pushV.pop(0)]

        while popV:

            if stack[-1] == popV[0]:
                popV.pop(0)
                stack.pop()

            elif pushV:
                stack.append(pushV.pop(0))

            else:
                return False

        return True






