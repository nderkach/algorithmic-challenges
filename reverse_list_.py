class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

a = LinkedListNode('A')
# b = LinkedListNode('B')
# c = LinkedListNode('C')
# d = LinkedListNode('D')
# e = LinkedListNode('E')


# a.next = b
# b.next = c
# c.next = d
# d.next = e

def print_from(node):
    while node:
        print(node.value)
        node = node.next

def reverse_list(head):
    cur_node = head
    prev_node = None
    next_node = None
    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node
    return prev_node

def reverseList(head):
    
    stack = []
    
    if not head:
        return None
    
    node = head
    while node.next:
        stack.append(node)
        node = node.next
    
    new_head = node
    while stack:
        node.next = stack.pop()
        node = node.next
       
    node.next = None

    return new_head

print_from(a)
new_head = reverseList(a)
print_from(new_head)

