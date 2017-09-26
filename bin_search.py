def bin_search(a, start, end, n):
    if start > end:
        return False
    else:
        pivot = start + (end-start)//2
        # print(pivot)
        if a[pivot] == n:
            print(pivot)
            return True
        else:
            if n > a[pivot]:
                return bin_search(a, pivot+1, end, n)
            else:
                return bin_search(a, start, pivot-1, n)


# a = [1, 3, 4, 5, 7]

# bin_search(a, 0, len(a), 3)

a = [3, 4, 1, 2, 5]

# def unique(a):
#     a = sorted(a)
#     for i in range(len(a)-1):
#         if bin_search(a, i+1, len(a), a[i]):
#             return False
#     return True

# print(unique(a))

def unique(a):
    a = sorted(a)
    for i in range(len(a)-1):
        if bin_search(a, i+1, len(a), a[i]):
            return False
    return True

# print(unique(a))

def unique_hash(a):
    s = set()
    for i in range(len(a)):
        if a[i] in s:
            return False
        s.add(a[i])
    return True

print(unique_hash(a))





