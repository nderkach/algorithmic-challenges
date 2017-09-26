class MultiStack(object):

    def __init__(self, stacksize):
        self.totalstacks = 3
        self.array = [0] * stacksize * self.totalstacks
        self.sizes = [0] * self.totalstacks
        self.stacksize = stacksize

    def push(self, value, stacknum):
        if self.isFull(stacknum):
            raise Exception('Stack %d is full!'.format(stacknum))
        self.array[stacknum][self.sizes[stacknum]] = value
        self.sizes[stacknum] += 1

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack %d is empty!'.format(stacknum))
        total = self.sizes[stacknum]
        pop_value = self.array[stacknum * self.stacksize]
        for i in range(total-1):
            self.array[stacknum * self.stacksize + i] = self.array[stacknum * self.stacksize + i + 1]
        self.array[total-1] = 0
        self.sizes[stacknum] -= 1
        return pop_value

    def peak(self, stacknum):
         if self.isEmpty(stacknum):
            raise Exception('Stack %d is empty!'.format(stacknum))       
        return self.array[stacknum * self.stacksize]

    def isEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def isFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize




s = Stack(StackNode(1))
