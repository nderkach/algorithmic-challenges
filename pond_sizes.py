def traverse(a, row, col):
    if row < 0 or row >= len(a) or col < 0 or col >= len(a[0]) or a[row][col] != 0:
        return 0

    size = 1
    a[row][col] = -1

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            size += traverse(a, row+dr, col+dc)

    return size

def pond_sizes(a):
    counts = []
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 0:
                c = traverse(a, row, col)
                counts.append(c)
    return counts

a = [[0, 2, 1, 0],
     [0, 1, 0, 1],
     [1, 1, 0, 1],
     [0, 1, 0, 1]]

print(pond_sizes(a))