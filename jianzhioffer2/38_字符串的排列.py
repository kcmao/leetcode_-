def permutation(string):
    if string is None:
        return
    permutation_core(list(string), 0)

def permutation_core(list_str, index):
    if index > len(list_str):
        return

    if index == len(list_str):
        print("".join(list_str))

    for i in range(index, len(list_str)):
        list_str[index], list_str[i] = list_str[i], list_str[index]
        permutation_core(list_str,index+1)
        list_str[index], list_str[i] = list_str[i], list_str[index]

if __name__ == "__main__":
    permutation("abc")