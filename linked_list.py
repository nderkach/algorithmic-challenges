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


n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)


def print_list(node):
    while node.next:
        print(node, end=" ")
        node = node.next
    print(node)


def delete_by_value(head, value):
    node = head
    if node.data == value:
        return node.next

    while node.next:
        if node.next.data == value:
            node.next = node.next.next
            return head
        node = node.next

    return head

print_list(n1)
n1.append_to_tail(4)
print_list(n1)

new_head = delete_by_value(n1, 1)
print_list(new_head)


