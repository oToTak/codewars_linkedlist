''' task 2 '''
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    d = [el.strip() for el in s.split('->') if el.strip() != 'None'][::-1]
    prev = None
    for el in d:
        prev = Node(int(el), prev)

    return prev

def stringify(self):
    if self is None:
        return "None"
    if self.next is None:
        return f"{self.data} -> None"
    return f"{self.data} -> {stringify(self.next)}"

if __name__ == '__main__':
    a = linked_list_from_string('0 -> 1 -> 2 -> 3 -> None')
    print(a)
    print(stringify(a))
