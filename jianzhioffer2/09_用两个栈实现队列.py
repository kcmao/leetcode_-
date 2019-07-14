# -*- coding: utf-8 -*-
class Queue(object):
    """
    两个栈实现一个队列
    stack1作为缓冲区，enqueue都enqueue到stack1中
    dequeue从stack2 dequeue，当stack2为空再把stack1逆向倒到stack2中
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, data):
        self.stack1.append(data)

    def delete_head(self):
        if self.stack1 is None and self.stack2 is None:
            return
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


if __name__ == "__main__":
    q = Queue()
    q.append_tail(1)
    q.append_tail(2)
    q.append_tail(3)
    print(q.delete_head())
    print( )
    q.append_tail(4)
    print(q.delete_head())
    print(q.delete_head())
    print(q.delete_head())
