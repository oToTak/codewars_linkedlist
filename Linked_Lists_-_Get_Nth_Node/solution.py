''' task 4 '''

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    num = 0
    if index < 0 or node is None:
        raise Exception
    while True:
        if num == index:
            return node
        if node is None:
            raise Exception
        node = node.next
        num += 1
