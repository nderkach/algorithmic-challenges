class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def print_list(node):
    while node.next:
        print(node, end=" ")
        node = node.next
    print(node)

def remove_node(node):
    prev = node
    while node.next:
        node.data = node.next.data
        prev = node
        node = node.next
    prev.next = None

n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(7)
n2 = n1.next.next.next.next = Node(5)
n1.next.next.next.next.next = Node(9)


print_list(n1)

remove_node(n2)

print_list(n1)