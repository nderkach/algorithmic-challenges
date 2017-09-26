class Node(object):

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

n1 = Node(7)
n1.left = Node(4)
n1.left.left = Node(3)
n1.left.right = Node(5)
n1.left.right.right = Node(6)
n1.right = Node(9)
n1.right.left = Node(8)
n1.right.right = Node(13)


def in_order_rec(node, k, in_order_list):
    if not node:
        return None

    in_order_rec(node.left, k, in_order_list)
    in_order_list.append(node)
    in_order_rec(node.right, k, in_order_list)

def kth_smallest(node, k):
    in_order = []
    in_order_rec(node, k, in_order)
    print(in_order)
    return in_order[k-1].val

print(kth_smallest(n1, 3))



