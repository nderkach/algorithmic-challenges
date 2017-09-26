class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def append_to_tail(self, value):
        new_node = Node(value)
        node = self
        while node.next:
            node = node.next
        node.next = new_node

def print_list(node):
    while node.next:
        print(node, end=" ")
        node = node.next
    print(node)

def remove_duplicates(head):
    value_hash = set([head.data])
    while head and head.next:
        if head.next.data in value_hash:
            # remove element
            head.next = head.next.next
        else:
            value_hash.add(head.next.data)
            head = head.next

def remove_duplocates_nohash(head):
    i = head
    while i.next:
        j = i
        while j.next:
            if j.next.data == i.data:
                j.next = j.next.next
            else:
                j = j.next
        i = i.next

n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(2)
n1.next.next.next.next = Node(2)
n1.next.next.next.next.next = Node(1)


print_list(n1)

remove_duplocates_nohash(n1)

print_list(n1)