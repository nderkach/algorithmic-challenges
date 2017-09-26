# Hi Nikolay, all the best! Click on Join in top right corner when you are ready.

# Given a binary Tree, write methods to serialise and deserialise them into a list/array.

#     5
#    / \
#    7   9
#   / \ 
#  5   2
#  \
#   6

# [5, -7, 9, -7, 2, 6]
# 2 ** D

# {0: 1, 1: 2, 3: 2}
# 
#

'''
root, left/right, child (None = -5)

5, True, 7
7, True, 5
5, False, 2
5, -1, None
5, -2, 6
6, -1, -5
6, -2, -5
5, -2, 9
9, -1, -5
9, -2, -5
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# def serialize_rec(node, out=[]):
#     if not node:
#         return
#     serialize_rec(node.left, out)
#     out.append((node.data, True, node.left.data if node.left else None))
#     out.append((node.data, False, node.right.data if node.right else None))
#     serialize_rec(node.right, out)
    
    
# def serialize(node):
#     serialized = []
#     serialize_rec(node, serialized)
#     return serialized

# def deserialize(ilist):
#     node = None
#     root = None
#     for element in ilist:
#         if not node:
#             node = Node(element.data)
#             root = node
#         elif not element[2]:
#             if element[1]:
#                 node.left = Node(element.data)
#             else:
#                 node.right = Node(element.data)
        
#     return root

class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.data))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.right.left = Node(7)
n1.right.right = Node(9)
n1.left.left = Node(4)
n1.left.left.left = Node(0)
n1.left.right = Node(5)

c = Codec()
s = c.serialize(n1)
print(s)

        