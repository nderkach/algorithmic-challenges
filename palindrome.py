from collections import Counter

def palindrome_perm(s):
    s = ''.join(s.lower().split())
    c = Counter(s)
    count = 0
    for e in c.values():
        if e % 2 != 0:
            count += 1

    return count <= 1

assert palindrome_perm("Tae Coa") == False
assert palindrome_perm("Tact Coa") == True