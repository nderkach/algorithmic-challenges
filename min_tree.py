class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def dfs(node):
    if not node:
        return
    print(node.value, end=" ")
    dfs(node.left)
    dfs(node.right)

def bst_create(a, s, f):
    if s >= f:
        return None
    p = (f + s) // 2 
    n = Node(a[p])
    n.left = bst_create(a, s, p)
    n.right = bst_create(a, p+1, f) 
    return n

a = [0, 1, 3, 7, 8, 9]

root = bst_create(a, 0, len(a))

dfs(root)