class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')


a.next = b
b.next = c
c.next = d
d.next = e
e.next = c 


def print_from(node):
    traversed = set()
    while node:
        if node in traversed:
            break
        traversed.add(node)
        print(node.value)
        node = node.next

def has_cycle(node):
    first_runner = node
    second_runner = node
    while second_runner != None and second_runner.next != None:
        first_runner = first_runner.next
        second_runner = second_runner.next.next
        if first_runner == second_runner:
            # loop
            return True
    return False

print_from(a)
print(has_cycle(a))

