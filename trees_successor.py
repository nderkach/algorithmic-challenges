class Node(object):

    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self):
        return str(self.data)

n1 = Node(5)
n1.left = Node(2, n1)
n1.left.left = Node(1, n1.left)
n1.left.right = Node(3, n1.left)
n1.left.right.right = Node(4, n1.left.right)
n1.right = Node(8, n1)
n1.right.left = Node(6, n1.right)
n1.right.right = Node(9, n1.right)
n1.right.right.right = Node(10, n1.right.right)


def find_successor(node):
    if node.right:
        return node.right
    elif node.parent.left == node:
        return node.parent
    else:
        orig = node.data
        while node.parent:
            node = node.parent # go to the root
        if node.data >= orig:
            return node
        else:
            return None


assert find_successor(n1.left) == n1.left.right
assert find_successor(n1.left.left) == n1.left
assert find_successor(n1.left.right.right) == n1
assert find_successor(n1.right.left) == n1.right
assert find_successor(n1.right.right.right) == None