class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.right.left = Node(7)
n1.right.right = Node(9)
n1.left.left = Node(4)
n1.left.left.left = Node(0)
n1.left.right = Node(5)


def is_balanced(tree_root):

    # a tree with no nodes is superbalanced, since there are no leaves!
    if tree_root is None:
        return True

    depths = []  # we short-circuit as soon as we find more than 2

    # we'll treat this list as a stack that will store tuples of (node, depth)
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):
        print([(n[0].data, n[1]) for n in nodes])
        # pop a node and its depth from the top of our stack
        node, depth = nodes.pop()
        print(node.data, depth)

        # # case: we found a leaf
        if (not node.left) and (not node.right):
            pass

        #     # we only care if it's a new depth
        #     if depth not in depths:
        #         depths.append(depth)

        #         # two ways we might now have an unbalanced tree:
        #         #   1) more than 2 different leaf depths
        #         #   2) 2 leaf depths that are more than 1 apart
        #         if (len(depths) > 2) or \
        #                 (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
        #             return False

        # case: this isn't a leaf - keep stepping down
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True

print(is_balanced(n1))
