def coin_pick(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += \
                ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]


def change_possibilities_top_down(amount_left, denominations, current_index=0):
    # base cases:
    # we hit the amount spot on. yes!
    if amount_left == 0:
        return 1

    # we overshot the amount left (used too many coins)
    if amount_left < 0:
        return 0

    # we're out of denominations
    if current_index == len(denominations):
        return 0

    print "checking ways to make %i with %s" % \
        (amount_left, denominations[current_index:])

    # choose a current coin
    current_coin = denominations[current_index]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += \
            change_possibilities_top_down(amount_left, denominations,
                                          current_index + 1)
        amount_left -= current_coin

    return num_possibilities


# print(coin_pick(5, [1]))

change_possibilities_top_down(5, [1, 2, 3])
