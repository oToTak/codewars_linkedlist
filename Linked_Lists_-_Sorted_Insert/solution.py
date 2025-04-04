''' task 6 '''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def inserrt(head, data, place):
    start = head
    for _ in range(place):
        start = start.next

    start = Node(data, start)

    return head
    

def sorted_insert(head, data):
    start = head
    num = 0
    while True:
        if start.data < data and start.next.data > data:
            return inserrt(head, data, num+1)
        num += 1
        start = head.next

if __name__ == '__main__':
    a = sorted_insert(Node(1, (Node(2, Node(7, Node(8))))), 6)
    print(a)
