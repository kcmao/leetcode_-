def print_matrix_clock_wisely(matrix):

    left = 0
    right = len(matrix[0]) - 1
    up = 0
    down = len(matrix) - 1

    if matrix is None or matrix[0] is None or len(matrix) == 0 or len(matrix) == 0:
        return

    direction = 0
    while True:

        if direction == 0:
            for i in range(left, right+1):
                print(matrix[up][i])
            up += 1
        elif direction == 1:
            for i in range(up,down+1):
                print(matrix[i][right])
            right -=1

        elif direction == 2:
            for i in range(right, left-1, -1):
                print(matrix[down][i])
            down -= 1

        else:
            for i in range(down, up - 1, -1):
                print(matrix[i][left])
            left += 1

        if left > right or up > down:
            break
        direction = (direction + 1) % 4

    return



if __name__ =="__main__":
    matrix = [[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9,  10, 11, 12],
              [13, 14, 15, 16]]

    print_matrix_clock_wisely(matrix)

