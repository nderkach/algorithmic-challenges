def bit_diff(n1, n2):
    x = n1 ^ n2
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c

print(bit_diff(3, 2))