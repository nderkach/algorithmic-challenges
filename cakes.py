def max_value(cake_tuples, capacity):
    max_value = 0
    cake_tuples = [c for c in cake_tuples if c[0] != 0]
    cake_tuples.sort(key=lambda x: -x[1]/x[0])
    current_capacity = 0
    print(cake_tuples)
    for t in cake_tuples:
        while current_capacity + t[0] <= capacity:
            max_value += t[1]
            current_capacity += t[0]
    return max_value

# cake_tuples = [(7, 160), (3, 90), (2, 15)]
# cake_tuples = [(15, 160), (3, 90), (2, 15), (3, 40)]
cake_tuples = [(1, 30), (0, 20)]

capacity = 100

print(max_value(cake_tuples, capacity))