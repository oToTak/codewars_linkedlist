''' task 6 '''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{self.data} -> {self.next}" if self.next else f"{self.data}"

def sorted_insert(head, data):
    new_node = Node(data)

    if head is None or data < head.data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head

if __name__ == '__main__':
    a = sorted_insert(Node(1, Node(2, Node(7, Node(8)))), 6)
    print(a)
