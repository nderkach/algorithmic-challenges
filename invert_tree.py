from collections import deque

class Node(object):

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

n1 = Node(4)
n1.left = Node(2)
n1.left.left = Node(1)
n1.left.right = Node(3)
n1.right = Node(7)
n1.right.left = Node(6)
n1.right.right = Node(9)

def bfs(node):
    d = deque([node])
    while d:
        p = d.popleft()
        print(p)
        if p.left:
            d.append(p.left)
        if p.right:
            d.append(p.right)

def invert(node):
    if node:
        node.left, node.right = invert(node.right), invert(node.left)
        return node

invert(n1)
bfs(n1)

