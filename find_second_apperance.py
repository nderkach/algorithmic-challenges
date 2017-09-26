def find_second(a):
    n = len(a) - 1
    s = n*(n+1)//2
    return sum(a) - s

print(find_second([1, 3, 2, 4, 4]))
