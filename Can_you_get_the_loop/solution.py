''' task -1 '''

class Node():
    def __init__(self, next = None):
        self.next = next

def loop_size(node):
    fast = node
    slow = node

    while True:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            counter = 0
            while True:
                fast = fast.next 
                counter += 1
                if fast == slow:
                    return counter
            raise Cringe

if __name__ == '__main__':
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node5 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2

    print(loop_size(node1))
