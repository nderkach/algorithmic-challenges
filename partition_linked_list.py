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

def partition(node, k):
    rest = []; head = node
    while node.next:
        if node.next.data >= k:
            rest.append(node.next.data)
            node.next = node.next.next
        else:
            node = node.next

    for e in rest:
        node.next = Node(e)
        node = node.next

    return head

n1 = Node(3)
n1.next = Node(5)
n1.next.next = Node(8)
n1.next.next.next = Node(5)
n1.next.next.next.next = Node(10)
n1.next.next.next.next.next = Node(2)
n1.next.next.next.next.next.next = Node(1)

print_list(n1)

head = partition(n1, 5)

print_list(head)