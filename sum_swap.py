def sum_swap(a1, a2):
    diff = (sum(a1) - sum(a2)) // 2
    print(diff)
    s = set([e + diff for e in a2])
    print(s)
    for e in a1:
        if e in s:
            return (e, e - diff)
    return None

print(sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))