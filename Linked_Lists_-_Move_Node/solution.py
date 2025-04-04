''' task 5 '''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    dest = Node(source.data, dest)
    return Context(source.next, dest)

def stringify(self):
    if self is None:
        return "None"
    if self.next is None:
        return f"{self.data} -> None"
    return f"{self.data} -> {stringify(self.next)}"

if __name__ == "__main__":
    source = Node(1, Node(2, Node(3)))
    dest = Node(4, Node(5, Node(6)))

    a = move_node(source, dest)
    print('rse')
    print(stringify(a.source))
    print(stringify(a.dest))
