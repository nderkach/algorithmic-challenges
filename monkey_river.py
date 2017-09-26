def inner(e, _a, d, pos):
    _a[pos[e]] = 1
    gap = 0
    for c in _a:
        gap += 1
        if gap > d:
            return False
        if c == 1:
            gap = 0
    if gap >= d:
        return False
    return True


def monkey_river(a, d):
    if d > len(a):
        return 0

    pos = {}
    for i, e in enumerate(a):
        pos[e] = i

    s = sorted(a)
    _a = [0] * len(a)
    for e in filter(lambda x: x != -1, s):
        if inner(e, _a, d, pos):
            return e

    return -1

assert monkey_river(a=[1, -1, 0, 2, 3, 5], d=3) == 2
assert monkey_river(a=[3, 2, 1], d=1) == 3
assert monkey_river(a=[1, 2, 3, 4, -1, -1, -1], d=3) == -1

# [-1, 0, 1, 2, 3, 5]
# 0: [0, 0, 1, 0, 0, 0]
# 1: [1, 0, 1, 0, 0, 0]
# 2: [1, 0, 1, 1, 0, 0]
# 3: [1, 0, 1, 1, 1, 0]
