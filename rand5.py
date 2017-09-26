from random import randint

def rand7():
    return randint(1, 7)

def rand5():# 1-5
    while True:
        r = rand7()
        if r <= 5:
            break
    return r

print(rand5())