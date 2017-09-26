import itertools


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = list(itertools.chain(*vec2d))
        self.current_i = 0

    def next(self):
        """
        :rtype: int
        """
        c = self.vec2d[self.current_i]
        self.current_i += 1
        return c

    def hasNext(self):
        """
        :rtype: bool
        """

        return self.current_i < len(self.vec2d) - 1


# Your Vector2D object will be instantiated and called as such:
vec2d = [
  [1,2],
  [3],
  [4,5,6]
]
i, v = Vector2D(vec2d), []
# print([_ for _ in i.vec2d])
while i.hasNext():
    t = i.next()
    print(t)

print(v)
