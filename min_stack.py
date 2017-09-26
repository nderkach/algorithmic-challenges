class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev_min = None

class MultiStack(object):

    def __init__(self):
        self.min = float('inf')
        self.top = None

    def push(self, value):
        n = StackNode(value)
        if value < self.min:
            n.prev_min = self.min
            self.min = value
        if not self.top:
            self.top = n
        else:
            n.next = self.top
            self.top = n

    def pop(self):
        if self.is_empty():
            raise Exception('Stack %d is empty!'.format(stacknum))
        pop_n = self.top
        self.top = self.top.next
        if pop_n.data == self.min:
            self.min = pop_n.prev_min
        return pop_n.data

    def peak(self):
        if self.is_empty():
            raise Exception('Stack %d is empty!'.format(stacknum))       
        return self.top.data

    def is_empty(self):
        return self.top == None


stack = MultiStack()
stack.push(3)
stack.push(4)

print(stack.min)

stack.push(2)

print(stack.min)

stack.push(1)

print(stack.min)

print(stack.pop())

print(stack.min)




