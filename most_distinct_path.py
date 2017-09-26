max_l = 1

class Node(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

n1 = Node(4)
n1.left = Node(5)
n1.left.left = Node(4)
n1.left.left.left = Node(7)
n1.right = Node(6)
n1.right.left = Node(1)
n1.right.right = Node(6)

def max_most_distinct(node, prev=None, length=1):
    if not node:
        return
    global max_l
    if length > max_l:
        max_l = length
    print(node.data, prev)
    max_most_distinct(node.left, prev=node.data, length=length if node.data == prev else length + 1)
    max_most_distinct(node.right, prev=node.data, length=length if node.data == prev else length + 1)

max_most_distinct(n1)

print(max_l)