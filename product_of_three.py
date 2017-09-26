from itertools import islice

def product_of_three(numbers):
    lowest = min(numbers[0], numbers[1])
    highest = max(numbers[0], numbers[1])
    lowest_product_of_2 = numbers[0] * numbers[1]
    highest_product_of_2 = numbers[0] * numbers[1]
    highest_product_of_3 = numbers[0] * numbers[1] * numbers[2]
    for num in islice(numbers, 2, None):
        highest_product_of_3 = max(highest_product_of_3, lowest_product_of_2 * num, highest_product_of_2 * num)
        lowest_product_of_2 = min(lowest_product_of_2, lowest * num, highest * num)
        highest_product_of_2 = max(highest_product_of_2, highest * num, lowest * num)
        lowest = min(lowest, num)
        highest = max(highest, num)
    return highest_product_of_3

print(product_of_three([-10, -10, 1, 3, 2]))
print(product_of_three([1, 10, -5, 1, 100]))