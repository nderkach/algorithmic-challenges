class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


def print_from(node):
    while node:
        print(node.value)
        node = node.next

def delete_node(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        raise Exception("last node")

# print_from(a)
delete_node(c)
print(c)
print_from(a)

