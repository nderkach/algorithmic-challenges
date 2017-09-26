from collections import deque

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = None

class ListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


n1 = Node(3)
n1.left = Node(7)
n1.left.right = Node(6)
n1.left.left = Node(9)
n1.left.left.left = Node(3)
n1.left.left.right = Node(4)
n1.right = Node(1)
n1.right.left = Node(2)
n1.right.right = Node(5)



def bfs_level(node):
    node.level = 0
    d = deque([node])
    h = {}
    while d:
        e = d.popleft()
        if e.level not in h:
            h[e.level] = ListNode(e.value)
        else:
            t = h[e.level]
            while t.next:
                t = t.next
            t.next = ListNode(e.value)
        if e.left:
            e.left.level = e.level + 1
            d.append(e.left)
        if e.right:
            e.right.level = e.level + 1
            d.append(e.right)
    return h

# h = bfs_level(n1)

# def dfs_level(node, h={}, level=0):
#     if not node:
#         return 
#     if level not in h:
#         h[level] = ListNode(node.value)
#     else:
#         t = h[level]
#         while t.next:
#             t = t.next
#         t.next = ListNode(node.value)
#     dfs_level(node.left, h, level+1)
#     dfs_level(node.right, h, level+1)
#     return h

# h = dfs_level(n1)

# for key in h:
#     print(key, end=": ")
#     while h[key]:
#         print(h[key].value, end=" ")
#         h[key] = h[key].next
#     print()

def check_balanced(root):
    return abs(dfs_count(root.left) - dfs_count(root.right)) <= 1

def dfs_count(n):
    if not n:
        return 0
    elif not n.left and not n.right:
        return 1
    else:
        return dfs_count(n.left) + dfs_count(n.right) + 1

print(check_balanced(n1))

