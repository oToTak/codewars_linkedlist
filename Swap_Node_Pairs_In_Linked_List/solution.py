''' task 9 '''

class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    a, b, c = head, head.next, head.next.next

    b = a
    a = swap_pairs(c)

    return b

if __name__ == '__main__':
    anode = Node(Node(None))
    swap_pairs(anode)
