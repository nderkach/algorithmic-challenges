import math

def is_prime(n):
    if n > 1:
        prime = True
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if not n % i:
            print(i)
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not prime")

is_prime(841)