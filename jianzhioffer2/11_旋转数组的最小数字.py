# -*- coding: utf-8 -*-
#关键是确定循环结束的条件，一定是第二个指针恰好比第一个指针大一
#这样就能退出，不然无限循环


def find_in_order(order_li):
    if order_li is None:
        return

    first = 0
    second = len(order_li) - 1

    mid = second // 2


    while first <= second:
        if second - first == 1:
            return order_li[second]
        if order_li[mid] > order_li[first]:
            first = mid
            mid = (first+second) // 2
        else:
            second = mid
            mid = (first+second) // 2
    return order_li[first]



if __name__ == "__main__":
    print(find_in_order([3, 4, 5, 1, 2]))
    print(find_in_order([1, 1, 1, 1, 1]))