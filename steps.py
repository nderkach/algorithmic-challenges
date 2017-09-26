def steps(n, s={}):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if n in s:
            return s[n]
        else:
            s[n] = steps(n-1) + steps(n-2) + steps(n-3)
            return s[n]

# print(steps(1))
# print(steps(2))
# print(steps(3))
# print(steps(4))
# print(steps(5))
print(steps(20))