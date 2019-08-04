class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def FindKthToTail(Head, k):
    if Head is None or k == 0:
        return
    first = Head
    second = Head

    for i in range(k-1):
        if first.next is not None:
            first = first.next
        else:
            return

    while first.next:
        first = first.next
        second = second.next
    return second

if __name__ == "__main__":
    l1_5 = Node(5)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head = l1_1
    print(FindKthToTail(head, 0).value)
