''' task -2 '''
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise Cringe

    flag = True
    start = head
    first = []
    second = []

    while True:
        if flag is True:
            load = first
            flag = False
        elif flag is False:
            load = second
            flag = True

        load.append(start.data)

        if start.next is None:
            break

        start = start.next

    first = first[::-1]
    second = second[::-1]

    def list_to_reversed_linlist(s):
        prev = None
        for el in s:
            prev = Node(int(el), prev)

        return prev

    a = list_to_reversed_linlist
    return Context(a(first), a(second))
