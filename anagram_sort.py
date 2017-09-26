from collections import defaultdict
from itertools import chain

def is_anagram(a1, a2):
    return sorted(a1) == sorted(a2)

# def anasort(arr):
#     h = defaultdict(list)
#     for e in a:
#         h[''.join(sorted(e))].append(e)

#     return list(chain(*h.values()))

def anasort(arr):
    return sorted(arr, key=lambda x: sorted(x))



a = ["abcd", "feta", "etst", "ttes", "atef"]
print(anasort(a))