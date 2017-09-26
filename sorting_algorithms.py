def partition(a, left, right, pivot):
    pivot = a[(left+right)//2]
    while left <= right:
        while a[left] < pivot:
            left += 1
        while a[right] > pivot:
            right -= 1

        if left <= right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

    return left

def quicksort_helper(a, left, right):
    if left >= right:
        return a
    index = partition(a, left, right)
    if left < index - 1:
        quicksort_helper(a, left, index-1)
    else:
        quicksort_helper(a, index+1, right)

def quicksort(a):
    left, right = 0, len(a)-1
    return quicksort_helper(a, left, right)

print(quicksort([5, 3, 1, 8, 2]))