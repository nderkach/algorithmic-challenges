from enum import Enum
max_l = 0

from collections import deque


class Direction(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2


class Node(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

n1 = Node(1)
n1.left = Node(2)
n1.left.left = Node(9)
n1.right = Node(3)
n1.right.left = Node(4)
n1.right.right = Node(5)
n1.right.left.right = Node(8)
n1.right.right.right = Node(6)

#       1
#      / \
#     2   3
#    /   / \
#   9   4   5
#        \   \
#         8   6


# def max_zigzag(node, direction=Direction.NONE, length=0):
#     if not node:
#         return
#     global max_l
#     if length > max_l:
#         max_l = length
#     max_zigzag(node.left, direction=Direction.LEFT, length=length if direction in (
#         Direction.NONE, Direction.LEFT) else length + 1)
#     max_zigzag(node.right, direction=Direction.RIGHT, length=length if direction in (
#         Direction.NONE, Direction.RIGHT) else length + 1)

# max_zigzag(n1)
# assert(max_l == 2)

# def bfs(node):
#     q = deque([node])
#     visited = set()
#     while q:
#         current = q.popleft()
#         print(current.data, end=" ")
#         if current.left and current.left not in visited:
#             q.append(current.left)
#         if current.right and current.right not in visited:
#             q.append(current.right)

def topView(root):
    q = deque([root])
    visited = set()
    direction = None
    while q:
        current = q.popleft()
        print(current.data, end = " ")
        if current.left and current.left not in visited and (direction in (None, 'left') or not current.right):
            q.append(current.left)
        if current.right and current.right not in visited and (direction in (None, 'right') or not current.left):
            q.append(current.right)
        if not direction:
            direction = 'left'
        elif direction == 'left':
            direction = 'right'
        elif direction == 'right':
            direction = 'left'


topView(n1)