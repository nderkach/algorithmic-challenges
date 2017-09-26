def get_max_number(a):
    print(a)
    l = [a[0]]
    for i in range(1, len(a)):
        new_row = []
        for el in l:
            new_row.append(el + a[i])
            new_row.append(el - a[i])
            new_row.append(el * a[i])
            if a[i] != 0:
                new_row.append(el / a[i])
        l = [min(new_row), max(new_row)]

    return max(l)

print(get_max_number((1, 12, 3)))
print(get_max_number((1, 12, -3)))