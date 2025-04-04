""" task7 """

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def reverse(head):
    start = head
    res = None
    while True:
        if start is None:
            break

        res = Node(start.data, res)

        start = start.next 

    return res


if __name__ == '__main__':
    b = Node(1, (Node(2, Node(7, Node(8)))))
    a = reverse(b)
    print(a)
