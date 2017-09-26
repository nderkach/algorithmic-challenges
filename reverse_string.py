def reverse(s):
    a = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return ''.join(a)

print(reverse("testinge"))