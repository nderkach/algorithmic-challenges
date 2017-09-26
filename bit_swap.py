def bit_swap(n):
    print(bin(n))
    s = n
    even_bits = n & 0x55555555 
    odd_bits = n & 0xaaaaaaaa
    print(bin(even_bits))
    print(bin(odd_bits))
    even_bits <<= 1
    odd_bits >>= 1
    s = even_bits | odd_bits
    print(bin(s))

bit_swap(1943)