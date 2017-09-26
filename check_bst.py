class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n1 = Node(1)
n1.left = Node(0)
n1.right = Node(2)
n1.right.right = Node(3)
n1.right.left = Node(-1)
# n1.left.right = Node(6)
# n1.left.left = Node(9)
# n1.left.left.left = Node(3)
# n1.left.left.right = Node(4)
# n1.right.left = Node(2)
# n1.right.right = Node(5)


def check_bst(n, left, right):
    if not n:
        return True
    else:
        return left < n.value < right and check_bst(n.left, left, n.value) and check_bst(n.right, n.value, right)

print(check_bst(n1, -float('inf'), float('inf')))
