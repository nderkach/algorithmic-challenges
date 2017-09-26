from collections import Counter

def check(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2

def check_hashmap(s1, s2):
    if len(s1) != len(s2):
        return False
    c = Counter(s1)
    for e in s2:
        c[e] -= 1
    return all([t == 0 for t in c.values()]) 

assert check_hashmap("abcf", "dacb") == False
assert check_hashmap("abcd", "dacb") == True
