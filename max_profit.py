def get_max_profit(a):
    least_price = a[0]
    max_profit = a[1] - a[0]
    for cur_time, cur_price in enumerate(a[1:]):
        max_profit = max(cur_price-least_price, max_profit)
        least_price = min(cur_price, least_price)
    return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday = [1, 1, 1, 1, 1, 1]
# stock_prices_yesterday = [6, 5, 4, 2]

print(get_max_profit(stock_prices_yesterday))