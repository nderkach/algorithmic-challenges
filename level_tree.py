from collections import deque, defaultdict

class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = deque()
        levels = defaultdict(list)
        d.append(root)
        level = 0
        levels[level].append(root)
        
        while d:
            p = d.popleft()
            level += 1
            if p.left:
                d.append(p.left)
                levels[level].append(p.left)
            if p.right:
                d.append(p.right)
                levels[level].append(p.right)
        
        return [levels[k][-1] for k in levels]
        
# n1 = Node(1)
# n1.left = Node(2)
# n1.right = Node(3)
# n1.right.left = Node(7)
# n1.right.right = Node(9)
# n1.left.left = Node(4)
# n1.left.left.left = Node(0)
# n1.left.right = Node(5)

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.right.left = Node(5)
n1.right.right = Node(6)
# n1.left.left = Node(4)
# n1.left.left.left = Node(0)
# n1.left.right = Node(5)

s = Solution()
print(s.rightSideView(n1))