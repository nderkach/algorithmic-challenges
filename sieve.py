import math

def sieve(n):
    flags = [False, False] + [True]*(n-2)
    prime = 2
    while prime < math.sqrt(n):
        p = prime*prime
        while p < n:
            flags[p] = False
            p += prime
        prime = prime + 1
        while prime < n and not flags[prime]:
            prime += 1

    print([i for i, e in enumerate(flags) if e])

sieve(10)