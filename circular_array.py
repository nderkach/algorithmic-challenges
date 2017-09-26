class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return "{}".format(self.data)


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.total = 0

    def append(self, node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            current = self.head
            count = 0
            while count < self.total-1:
                current = current.next
                count += 1
            current.next = node
            node.prev = current
            self.head.prev = node
        self.total += 1

    def __iter__(self):
        current = self.head
        count = 0
        while count < self.total:
            yield current
            current = current.next
            count += 1


class CircularArray(LinkedList):

    def __init__(self):
        super().__init__()

    def shift_by(self, k):
        k = k % self.total
        if not k:
            return
        for _ in range(k):
            self.head = self.head.prev

    def __str__(self):
        return " ".join([str(e) for e in li])


li = CircularArray()
li.append(Node(1))
li.append(Node(2))
li.append(Node(3))
print(li)

li.shift_by(1)
print(li)




