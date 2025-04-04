''' task 8 '''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if head == None:
        return head
    current = head
    next = current.next
    while next:
        if current.data == next.data:
            current.next = current.next.next
            next = current.next
        else:
            current = next
            next = current.next
    return head


if __name__ == '__main__':
    b = Node(1, (Node(2, Node(7, Node(7, Node(8, Node(8)))))))
    a = remove_duplicates(b)
    print(a)
