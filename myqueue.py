class Stack:

    def __init__(self, stacksize=10):
        self.array = [0] * stacksize
        self.stacksize = stacksize
        self.size = 0

    def push(self, item):
        if self.IsFull():
            raise Exception('Stack is full')
        self.size += 1
        self.array[self.IndexOfTop()] = item

    def pop(self):
        if self.IsEmpty():
            return None
        value = self.array[self.IndexOfTop()]
        self.array[self.IndexOfTop()] = 0
        self.size -= 1
        return value

    def peek(self):
        if self.IsEmpty():
            return None
        return self.array[self.IndexOfTop()]

    def IsEmpty(self):
        return self.size == 0

    def IsFull(self):
        return self.size == self.stacksize

    def IndexOfTop(self):
        return self.size - 1


# s = Stack(10)
# s.push(4)
# s.push(5)
# print(s.peek())
# s.pop()
# print(s.peek())


class MyQueue(object):
    def __init__(self):
        self.top_stack = Stack()
        self.bottom_stack = Stack()

    def push(self, value):
        self.top_stack.push(value)
        tmp = self.top_stack
        self.bottom_stack = Stack()
        c = tmp.pop()
        while c:
            self.bottom_stack.push(c)
            c = tmp.pop()


    def pop(self):
        popped = self.bottom_stack.pop()
        tmp = self.bottom_stack
        self.top_stack = Stack()
        c = tmp.pop()
        while c:
            self.top_stack.push(c)
            c = tmp.pop()

    def first(self):
        return self.bottom_stack.peek()

    def last(self):
        return self.top_stack.peek()

m = MyQueue()

m.push(3)
m.push(4)

print(m.first())
print(m.last())

m.push(5)
m.push(7)

print(m.first())
print(m.last())
