class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def __str__(self):
        return ' '.join([str(v) for v in self.items])

class MaxStack:

    # initialize an empty list
    def __init__(self):
        self.items = []
        self.maxe = float('-inf')
        self.max_elements = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)
        if item > self.maxe:
            self.maxe = item
        self.max_elements.append(self.maxe)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        self.max_elements.pop()
        if self.max_elements:
            self.maxe = self.max_elements[-1]
        else:
            self.maxe = float('-inf')
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def __str__(self):
        return ' '.join([str(v) for v in self.items])

    def get_max(self):
        if self.maxe == float('-inf'):
            return None
        else:
            return self.maxe



s = MaxStack()
s.push(9)
s.push(7)
s.push(12)
s.push(1)
s.push(13)


print(s)

print(s.get_max())
s.pop()
print(s.get_max())
s.pop()
print(s.get_max())
s.pop()
print(s.get_max())
s.pop()
print(s.get_max())
s.pop()
print(s)
print(s.get_max())

