import collections


class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def verticalOrder(root):
    cols = collections.defaultdict(list)
    queue = collections.deque([(root, 0)])
    while queue:
        node, i = queue.popleft()
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.right.left = Node(7)
n1.right.right = Node(9)
n1.left.left = Node(4)
n1.left.left.left = Node(0)
n1.left.right = Node(5)

print(verticalOrder(n1))
