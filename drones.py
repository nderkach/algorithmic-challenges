from collections import Counter

# def find_unique(a):
#     c = Counter(a)
#     for key in c:
#         if c[key] == 1:
#             return key
#     return None

def find_unique(a):
    x = 0
    for e in a:
        x ^= e
    return x

a = [15, 13, 19, 15, 21, 5, 5, 13, 21]

print(find_unique(a))

