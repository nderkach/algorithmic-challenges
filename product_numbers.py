def product_numbers(a):
    products_of_all_ints_except_at_index = [None]*len(a)
    product_so_far = 1
    for i in range(len(a)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= a[i]

    product_so_far = 1
    for i in range(len(a)-1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= a[i]

    return products_of_all_ints_except_at_index

print(product_numbers([1, 7, 3, 4]))