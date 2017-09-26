class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def append_to_tail(self, value):
        new_node = Node(value)
        node = self
        while node.next:
            node = node.next
        node.next = new_node

def print_list(node):
    while node.next:
        print(node, end=" ")
        node = node.next
    print(node)

def return_kth_to_last(head, k):
    i = j = head
    c = 0
    while c != k:
        j = j.next
        c += 1
    while j.next:
        i = i.next
        j = j.next
    return i

n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(7)
n1.next.next.next.next = Node(5)
n1.next.next.next.next.next = Node(9)


print_list(n1)

print(return_kth_to_last(n1, 0))
