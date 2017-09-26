import math


def find_pivot(a):
    left = 0
    right = len(a) - 1
    while (left <= right):
        m = left + (right + 1 - left) // 2
        if m == 0 or a[m] < a[m - 1]:
            return m
        if a[0] < a[m]:
            left = m + 1
        else:
            right = m - 1
    return 0


def binary_search(a, e, left, right):
    while (left <= right):
        m = left + (right - left) // 2
        if e == a[m]:
            return m
        elif a[m] > e:
            right = m - 1
        else:
            left = m + 1
    return -1


def shifted_arr_search(shiftArr, num):
    if len(shiftArr) == 1:
        return 0
    p = find_pivot(shiftArr)

    if p == 0 or num < shiftArr[0]:
        return binary_search(shiftArr, num, p, len(shiftArr) - 1)
    else:
        return binary_search(shiftArr, num, 0, p - 1)

print(find_pivot([3, 1]))
print(find_pivot([1, 2, 3]))

# print(shifted_arr_search([1, 3], 1))
