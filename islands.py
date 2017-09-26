def get_adjacent(a, row, column):
    adjacent = []
    if a[row][column] == 0:
        return

    a[row][column] = 0
    if column < len(a[0]) - 1 and a[row][column+1] == 1:
        adjacent.append((row, column+1))
    if column > 1 and a[row][column-1] == 1:
        adjacent.append((row, column-1))
    if row > 1 and a[row-1][column] == 1:
        adjacent.append((row-1, column))
    if row < len(a) - 1 and a[row+1][column] == 1:
        adjacent.append((row+1, column))
    for e in adjacent:
        get_adjacent(a, e[0], e[1])


def get_number_of_islands(binaryMatrix):
    counter = 0
    for row in range(len(binaryMatrix)):
        for column in range(len(binaryMatrix[0])):
            if binaryMatrix[row][column] == 1:
                counter += 1
                get_adjacent(binaryMatrix, row, column)
    return counter

binaryMatrix = [[0,    1,    0,    1,    0],
                [0,    0,    1,    1,    1],
                [1,    0,    0,    1,    0],
                [0,    1,    1,    0,    0],
                [1,    0,    1,    0,    1]]

print(get_number_of_islands(binaryMatrix))
