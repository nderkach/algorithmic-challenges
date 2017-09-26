def bin_search(a, t, l, r):
    print(l, r)
    while l <= r:
        m = (l + r) // 2
        if a[m] < t:
            l = m + 1
        elif a[m] > t:
            r = m - 1
        else:
            return m
    return -1

def bin_search_mod(a, t, l=0, r=len):
    m = (l + r) // 2

    if t == a[m]:
        return m

    if l > r:
        return -1

    if a[l] < a[m]:
        if a[l] <= t < a[m]:
            return bin_search_mod(a, t, l, m-1)
        else:
            return bin_search_mod(a, t, m+1, r)
    elif a[l] > a[m]:
        if a[m] < t <= a[r]:
            return bin_search_mod(a, t, m+1, r)
        else:
            return bin_search_mod(a, t, l, m-1)
    elif a[l] == a[m]:
        if a[m] != a[r]:
            return bin_search_mod(a, t, m+1, r)
        else:
            r = bin_search_mod(a, t, l, m-1)
            if r == -1:
                return bin_search_mod(a, t, m+1, r)
            else:
                return r
    return -1

def bin_search_mod_(a, t):
    return bin_search_mod(a, t, 0, len(a)-1)


print(bin_search_mod_([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5))