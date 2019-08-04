def verify_sequence_of_BST(sequence):
    if sequence is None or len(sequence) <= 0:
        return False
    return verify_sequence_of_BST_core(sequence)

def verify_sequence_of_BST_core(sequence):
    if sequence is None or len(sequence) <= 1:
        return True
    length = len(sequence)

    root = sequence[-1]

    i = 0
    for j in range(length-1):
        if sequence[j] > root:
            i = j
            break

    for j in range(i, length-1):
        if sequence[j] < root:
            return False

    left = verify_sequence_of_BST_core(sequence[:i])

    right = verify_sequence_of_BST_core(sequence[i:length-1])


    return left and right

if __name__ == "__main__":
    print(verify_sequence_of_BST([5, 7, 6, 9, 11, 10, 8]))
    print(verify_sequence_of_BST([7, 4, 6, 5]))







