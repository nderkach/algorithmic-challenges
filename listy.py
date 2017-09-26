class Listy(object):
    def __init__(self, a):
        self.a = a

    def elemen_at(self, i):
        if i >= len(self.a) or i < 0:
            return -1
        else:
            return self.a[i]

    def __str__(self):
        return str(self.a)

    def get_len(self):
        if self.elemen_at(0) == -1:
            return 0
        i = 1
        while self.elemen_at(i) != -1:
            i *= 2
        # backtrack
        while self.elemen_at(i) == -1:
            i -= 1

        return i + 1

l = Listy([1, 4, 5, 8, 12])
print(l)
print(l.elemen_at(3))
print(l.get_len())