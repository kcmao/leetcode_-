def reOrderOddEven(data):
    if data is None or len(data) == 0:
        return
    first = 0
    second = len(data) - 1

    while first < second:
        #注意，while first < second 不能少
        while first < second and data[first] % 2 == 1:
            first += 1
        while first < second and data[second] % 2 == 0:
            second -= 1

        data[first], data[second] = data[second], data[first]

    print(data)
    return data

def Test(testname, data ):
    print(testname,)
    reOrderOddEven(data)

def Test1():

    numbers = [1, 2, 3, 4, 5, 6, 7]
    Test("Test1", numbers)


def Test2():

    numbers = [2, 4, 6, 1, 3, 5, 7]
    Test("Test2", numbers)


def Test3():

    numbers = [1, 3, 5, 7, 2, 4, 6]
    Test("Test3", numbers)


def Test4():

    numbers = [1]
    Test("Test4", numbers)


def Test5():

    numbers = [2]
    Test("Test5", numbers)


def Test6():

    Test("Test6","")





if __name__ == "__main__":
    Test1()
    Test2()
    Test3()
    Test4()
    Test5()
    Test6()