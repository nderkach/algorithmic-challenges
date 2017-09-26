from collections import deque

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

def sum(n1, n2):
    n = None
    r = 0

    while n1 or n2:
        a = n1.data if n1 else 0
        b = n2.data if n2 else 0
        s = (a + b + r) % 10
        r = (a + b + r) // 10
        if n:
            n.next = Node(s)
            n = n.next
        else:
            n = Node(s)
            head = n
        if n1:
            n1 = n1.next
        if n2:
            n2 = n2.next

    if r:
        n.next = Node(r)

    return head

def reverse(n):
    d = deque()

    while n.next:
        d.append(n.data)
        n = n.next

    n_rev = Node(n.data)
    n_rev_head = n_rev

    while d:
        n_rev.next = Node(d.pop())
        n_rev = n_rev.next

    return n_rev_head


n1 = Node(9)
n1.next = Node(0)
n1.next.next = Node(0)
n1.next.next.next = Node(0)

print_list(n1)

n2 = reverse(n1)

print_list(n2)

# n2 = Node(5)
# n2.next = Node(1)

# print_list(n1)
# print_list(n2)

# head = sum(n1, n2)

# print_list(head)

# n1 = Node(6)
# n1.next = Node(1)
# n1.next.next = Node(7)

# n2 = Node(2)
# n2.next = Node(9)
# n2.next.next = Node(5)

# print_list(n1)
# print_list(n2)

# head = sum(n1, n2)

# print_list(head)