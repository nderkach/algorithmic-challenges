def add_without_plus(a, b):
    add_without_carry = a ^ b
    while a or b:
        ca = a if a else 0
        cb = b if b else 0
        if (ca & 1) & (cb & 1):
            carry = 1
        else:
            carry = 0
        a >>= 1
        b >>= 1



print(add_without_plus(3, 5))