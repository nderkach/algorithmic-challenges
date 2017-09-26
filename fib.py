def fib(n, memo={}):
    if n in (1, 2):
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            print("computing ", n)
            m = fib(n-1, memo) + fib(n-2, memo)
            memo[n] = m
            return m


print(fib(10))