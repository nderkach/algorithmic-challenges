from collections import deque

class Graph(object):
    def __init__(self, nodes):
        self.nodes = None

class Node(object):
    def __init__ (self, name, children=[]):
        self.name = name
        self.children = children
        self.visited = False


n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")

graph = Graph([n1, n2, n3, n4])

#  A -> B
#  |  > ^ 
#  v /  |
#  C -> D
#

n1.children = [n3, n2]
n3.children = [n2]
n3.children = [n2, n4]
n4.children = [n2]

def dfs(node):
    if not node:
        print()
        return
    node.visited = True
    print(node.name, end=" ")
    for child in node.children:
        if not child.visited:
            dfs(child)

# dfs(n1)

def bfs(node):
    node.visited = True
    d = deque([node])
    while d:
        n = d.popleft()
        print(n.name, end=" ")
        for child in n.children:
            if not child.visited:
                child.visited = True
                d.append(child)

# bfs(n1)


def bfs_mod(node, find_n):
    node.visited = True
    d = deque([node])
    while d:
        n = d.popleft()
        if n == find_n:
            return True
        for child in n.children:
            if not child.visited:
                child.visited = True
                d.append(child)
    return False

def path_exists(n1, n2):
    return bfs_mod(n1, n2) or bfs_mod(n2, n1)

print(path_exists(n2, n4))
