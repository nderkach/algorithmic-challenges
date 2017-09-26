#!/usr/bin/env python


def rec_multiply(a, b):
    if a < b:
        a, b = b, a

    if b == 1:
        return a
    else:
        print("rec call")
        return rec_multiply(a, b - 1) + a

print(rec_multiply(3, 4))
