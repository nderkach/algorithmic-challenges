def rotate(a, n):
    b = []
    for row in range(n):
        new_row = []
        for col in range(n):
            new_row.append(a[n-1-col][row])
        b.append(new_row)
    print(b)

rotate([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]], 3)