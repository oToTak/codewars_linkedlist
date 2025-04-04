''' task 1 '''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(self):
    if self is None:
        return "None"
    if self.next is None:
        return f"{self.data} -> None"
    return f"{self.data} -> {stringify(self.next)}"

if __name__ == '__main__':
    a= stringify(Node(0, Node(1, Node(2, Node(3)))))
    print(a)
