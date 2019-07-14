# -*- coding: utf-8 -*-
def find_path_in_matrix(matrix, string):
    """
    :param matrix:
    :param string:
    :return:  True or False
    """
    if matrix is None or string is None:
        return False

    bool_matrix = []
    for i in range(len(matrix)):
        bool_matrix.append([])
        for j in range(len(matrix[0])):
            bool_matrix[i].append(0)

    path_length = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if has_path_core(row, col, matrix, string, path_length, bool_matrix):
                return True

    return False

def has_path_core(row, col, matrix, string, path_length, bool_matrix):
    #如果string到头了，就返回true
    if path_length == len(string):
        return True

    #如果边界，返回false
    if row < 0 or col < 0 or row > len(matrix) - 1 or col > len(matrix[0]) - 1:
        return False

    #如果命中
    has_path = False

    if string[path_length] == matrix[row][col] and bool_matrix[row][col] == 0:
        path_length += 1
        bool_matrix[row][col] = 1
        has_path = \
            has_path_core(row - 1, col, matrix, string, path_length, bool_matrix) or \
            has_path_core(row + 1, col, matrix, string, path_length, bool_matrix) or \
            has_path_core(row, col + 1, matrix, string, path_length, bool_matrix) or \
            has_path_core(row, col - 1, matrix, string, path_length, bool_matrix)
        if not has_path:
            #path_length -= 100    #这个感觉没什么用
            bool_matrix[row][col] = 0
            pass
    return has_path



if __name__ == "__main__":
    matrix = [
        ["a", "a", "a", "g"],
        ["c", "b", "c", "f"],
        ["j", "d", "e", "h"]
    ]
    string = "acjd"
    print(find_path_in_matrix(matrix=matrix, string=string))