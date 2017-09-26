from random import randint
from collections import Counter

def years(a):
    births = Counter([e[0] for e in a])
    deaths = Counter([e[1] for e in a])
    count = 0
    out_years = []
    for y in range(1900, 2001):
        if y in births:
            count += births[y]
        elif y in deaths:
            count -= deaths[y]
        out_years.append(count)

    mi = out_years.index(max(out_years))
    return (1900 + mi, out_years[mi])


a = [sorted([randint(1900, 2000), randint(1900, 2000)]) for _ in range(100)]
print(years(a))