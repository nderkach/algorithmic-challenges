from collections import defaultdict

def compression(s):
    d = []
    count = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            d.append((s[i-1], count))
            count = 1
        else:
            count += 1
    d.append((s[-1], count))
    out = "".join([t[0]+str(t[1]) for t in d])
    if len(out) >= len(s):
        return s
    else:
        return out


assert(compression("aabcccccaaa") == "a2b1c5a3")
assert(compression("bbaabcccccafa") == "bbaabcccccafa")
assert(compression("bbaabcccccfff") == "b2a2b1c5f3")