def zero_matrix(a, m, n):
    b = []
    for row in range(n):
        new_row = []
        for col in range(n):
            new_row.append(a[n-1-col][row])
        b.append(new_row)
    print(b)

zero_matrix([[1, 2, 3, 4],
             [4, 0, 6, 7],
             [7, 8, 9, 3]], 4, 3)