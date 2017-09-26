def insertion(n, m, i, j):
    print("0b"+n)
    nb, mb = int(n, 2), int(m, 2)
    mask = (1<<i)-1
    mask |= (1<<len(n))-1-((1<<(j+1))-1)
    print(bin(mask))
    nb &= mask
    nb |= (mb << i)
    return bin(nb)

print(insertion("10000000000", "10011", 2, 6))