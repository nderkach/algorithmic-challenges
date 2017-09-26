def string_search(a, t):
    first = 0
    last = len(a) - 1
    while first <= last:
        m = (first + last) // 2
        if a[m] == "":
            left = m - 1
            right = m + 1
            while left >= first and right <= last:
                if a[left] != "":
                    m = left
                    break
                if a[right] != "":
                    m = right
                    break
                left -= 1
                right += 1
       
        if a[m] < t:
            first = m + 1
        elif a[m] > t:
            last = m - 1
        else:
            return m
    return -1


a = ["at", "", "", "", "", "", "", "", "ball", "", "", "", ""]
print(string_search(a, "ball"))