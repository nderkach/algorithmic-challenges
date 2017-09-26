class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

def print_list(node):
    while node:
        print(node.val)
        node = node.next

def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    out = None
    carry = 0
    while l1 or l2:
        l1t = l1.val if l1 else 0
        l2t = l2.val if l2 else 0

        p = l1t + l2t + carry
        if p > 9:
            carry = 1
        else:
            carry = 0

        if not out:
            head = ListNode(p % 10)
            out = head
        else:
            out.next = ListNode(p % 10)
            out = out.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        out.next = ListNode(1)

    return head

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# print_list(l1)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# print_list(l2)

print_list(add_two_numbers(l1, l2))
