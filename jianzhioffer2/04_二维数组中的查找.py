def find_in_matrix(matrix, number):
    """
    :param matrix: [list] matrix
    :param number:  [int] target number
    :return: [bool] true or false
    """
    rows  = len(matrix)
    columns = len(matrix[0])

    if matrix is None or number is None:
        return False

    row = 0
    column = columns - 1
    while row < rows and column >= 0:
        if matrix[row][column] == number:
            return True
        elif matrix[row][column] > number:
            column -= 1
        else:
            row += 1
    return False


if __name__ == "__main__":
    m = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
    print(find_in_matrix(m, 100))