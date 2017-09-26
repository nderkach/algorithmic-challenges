from random import randint

def rand7():
    return randint(1, 5)

def rand7():
    while True:
        r = rand5() + rand5()
        if r <= 7:
            break
    return r

print(rand7())