def partial_sort(a):
    left_end = 0
    right_start = len(a) - 1
    max_left = a[left_end]
    min_right = a[right_start]
    while a[left_end+1] >= a[left_end]:
        left_end += 1
        max_left = max(max_left, a[left_end])
    while a[right_start-1] <= a[right_start]:
        right_start -= 1
        min_right = min(min_right, a[right_start])
    print(left_end, right_start)
    print(max_left, min_right)

    if left_end >= right_start:
        return -1 # sorted

    i = left_end + 1
    min_middle = max_middle = a[i]
    while i < right_start:
        min_middle = min(min_middle, min_right)
        max_middle = max(max_middle, max_left)
        i += 1

    print(min_middle, max_middle)

    while a[left_end] > min_middle:
        left_end -= 1

    while a[right_start] < max_middle:
        right_start += 1

    print(left_end+1, right_start-1)


partial_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])