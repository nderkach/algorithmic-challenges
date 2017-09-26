from collections import deque
import math

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def print_list(node, stop=float('inf')):
    s = 0
    while node.next and s < stop-1:
        print(node, end=" ")
        node = node.next
        s += 1
    print(node)

def loop(n):
    i = n
    j = n.next
    while i.next != j.next.next:
        i = i.next
        j = j.next.next

    return i

n1 = Node(9)
n1.next = Node(1)
n1.next.next = Node(2)
n1.next.next.next = Node(3)
n2 = n1.next.next.next.next = Node(6)
n1.next.next.next.next.next = Node(7)
n1.next.next.next.next.next.next = n2

print_list(n1, stop=6)

assert loop(n1) == n2

print(loop(n1).data)
