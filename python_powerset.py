def int_to_set(x, s):
    subsets = []
    k = x
    index = 0
    while k > 0:
        if k & 1:
            subsets.append(s[index])
        k >>= 1
        index += 1
    return subsets

def powerset(s):
    total_sets = 1 << len(s)
    all_subsets = []
    for k in range(total_sets):
        all_subsets.append(int_to_set(k, s))
    return all_subsets

s = [1, 2, 3]
print(powerset(s))

# print(int_to_set(3, s))

