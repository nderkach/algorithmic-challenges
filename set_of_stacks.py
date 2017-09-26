class SetOfStacks(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [0] * capacity
        self.total = 0
        self.numstacks = 1
        self.totals = [0]

    def push(self, value):
        self.array[self.total] = value
        if self.total % self.capacity == 0:
            self.numstacks += 1
            self.totals += [0]
            self.array += [0]*capacity
        self.total += 1
        self.totals[self.numstacks] += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Stack %d is empty!'.format(stacknum))
        popped = self.array[self.total-1]
        self.array[self.total-1] = 0
        self.total -= 1
        self.totals[self.numstacks] -= 1
        if self.totals[self.numstacks] == 0:
            self.numstacks -= 1
        return popped.data

    def peak(self):
        if self.is_empty():
            raise Exception('Stack %d is empty!'.format(stacknum))       
        return self.array[self.total-1]

    def pop_at(self, index):
        popped = self.array[self.capacity * index + self.totals[index]-1]
        self.totals[index] -= 1
        self.total -= 1

        return popped

    def is_empty(self):
        return self.total == 0


stack = MultiStack()




