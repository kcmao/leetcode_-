"""
// 面试题4：二维数组中的查找
// 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
// 照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
// 整数，判断数组中是否含有该整数。
"""

"""
优化后的方法，查找次数为行+列-1
"""

def find_in_matrix(matrix, number):
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or not isinstance(number, int):
        return False

    # matrix是list of list
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        if len(matrix[i]) != col:
            return False

        for j in range(col):
            if not isinstance(matrix[i][j], int):
                return False

    i = 0
    j = col - 1
    while i < row and j >= 0:
        if matrix[i][j] == number:
            return True, i, j

        if matrix[i][j] > number:
            j -= 1

        if matrix[i][j] < number:
            i += 1
    return False, None, None


if __name__ == "__main__":
    m = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
    print(find_in_matrix(m, 15))
