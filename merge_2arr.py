def merge(arr1, arr2):
    i = len(arr1) - 1
    j = len(arr2) - 1
    cur = len(arr1) + len(arr2) - 1
    print(arr1)
    print(arr2)
    arr1 = arr1 + [None]*len(arr2)
    while i >= 0 and j >=0:
        print(arr1)
        if arr1[i] > arr2[j]:
            arr1[cur] = arr1[i]
            i -= 1
        else:
            arr1[cur] = arr2[j]
            j -= 1
        cur -= 1
    print(arr1)


merge([1, 6, 9, 17], [3, 4, 8, 8, 12])