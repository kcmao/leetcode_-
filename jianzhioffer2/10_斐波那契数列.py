def fibonacci(n):
    f_1 = 0
    f_2 = 1
    if n == 0:
        return f_1
    if n == 1:
        return f_2

    x = 2
    while x <= n:
        f_x = f_2 + f_1
        f_2 = f_1
        f_1 = f_x
        x += 1
    return f_x

if __name__ == "__main__":
    print(fibonacci(6))