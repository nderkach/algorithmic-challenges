def is_single_riffle(half1, half2, shuffled_deck):

    shuffled_deck_index=0
    half1_index=0
    half2_index=0

    # base case we've hit the end of shuffled_deck
    while shuffled_deck_index != len(shuffled_deck):
        
        # if we still have cards in half1
        # and the "top" card in half1 is the same
        # as the top card in shuffled_deck
        if (half1_index < len(half1)) and \
                half1[half1_index] == shuffled_deck[shuffled_deck_index]:
            half1_index += 1

        # if we still have cards in half2
        # and the "top" card in half2 is the same
        # as the top card in shuffled_deck
        elif (half2_index < len(half2)) and \
                half2[half2_index] == shuffled_deck[shuffled_deck_index]:
            half2_index += 1

        # if the top card in shuffled_deck doesn't match the top
        # card in half1 or half2, this isn't a single riffle.
        else:
            return False

        # the current card in shuffled_deck has now been "accounted for"
        # so move on to the next one
        shuffled_deck_index += 1

    return True