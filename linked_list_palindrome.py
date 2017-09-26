from collections import deque
import math

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


def is_palindrome(n):
    d = deque()
    head = n
    while n:
        d.append(n.data)
        n = n.next

    while d:
        if head.data != d.pop():
            return False
        head = head.next

    return True

def is_palindrome_rec(n, length):
    if length <= 1:
        return True
    else:
        head = n
        c = 0
        while n.next and c < length:
            n = n.next
            c += 1

        return head.data == n.data and is_palindrome_rec(n.next, length-2)
    

# n1 = Node(9)
# n1.next = Node(0)
# n1.next.next = Node(0)
# n1.next.next.next = Node(0)

# print_list(n1)

# n2 = Node(7)
# n2.next = Node(1)
# n2.next.next = Node(7)

# print_list(n2)

# assert is_palindrome(n1) == False
# assert is_palindrome(n2) == True

n1 = Node(9)
n1.next = Node(1)
n1.next.next = Node(2)
n1.next.next.next = Node(3)

print_list(n1)

n2 = Node(7)
n2.next = Node(1)
n2.next.next = Node(7)

print_list(n2)

assert is_palindrome_rec(n1, 4) == False
assert is_palindrome_rec(n2, 3) == True

