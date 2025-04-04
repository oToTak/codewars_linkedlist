''' task 8 '''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    endflag = True
    while True:
        if endflag is False:
            break

        start = head
        endflag = False
        while True:
            if start is None:
                break

            if not start.next is None and start.data == start.next.data:
                start = Node(start.data, start.next.next)
                endflag = True
            start = start.next

    return head

if __name__ == '__main__':
    b = Node(1, (Node(2, Node(7, Node(7, Node(8))))))
    a = remove_duplicates(b)
    print(a)
