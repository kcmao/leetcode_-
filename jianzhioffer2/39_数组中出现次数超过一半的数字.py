def more_than_half_num(numbers):
    if numbers is None or len(numbers) == 0:
        return 0
    result = numbers[0]
    count = 1
    for i in range(1, len(numbers)):

        if result == numbers[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            result = numbers[i]
            count = 1

    if verify(numbers, result):
        return result
    else:
        return 0


def verify(numbers, result):
    count = 0
    for i in numbers:
        if result == i:
            count += 1
    return count > len(numbers) / 2




if __name__ == "__main__":
    print(more_than_half_num([1,3,3,3,2,5,3,4,3]))
