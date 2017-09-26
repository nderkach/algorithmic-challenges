import random

SUITS = ['H', 'S', 'D', 'C']
VALUES = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']


class Card(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + self.suit


class DeckOfCards(object):
    def __init__(self):
        self.init_cards()

    def __iter__(self):
        for card in self.cards:
            yield card

    def init_cards(self):
        self.cards = [Card(suit, value) for value in VALUES for suit in SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        return ' '.join([str(card) for card in self])

class BJDeckOfCards(DeckOfCards):
    def __init__(self):
        super().__init__()
        self.game = []

    def reset_game(self):
        self.init_cards()
        self.game = []

    def count_cards(self):
        score = 0
        aces_count = 0
        for card in self.game:
            if card.value in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
                score += int(card.value)
            elif card.value in ('J', 'Q', 'K'):
                score += 10
            elif card.value == 'A':
                aces_count += 1

        while aces_count > 0:
            score += 11 if (score + 11) <= 21 else 1
            aces_count -= 1

        return score

    def pick(self):
        card = self.cards.pop()
        self.game.append(card)
        return card

d = BJDeckOfCards()
print(d)
print(d.pick())
print("score: ", d.count_cards())
print(d.pick())
print("score: ", d.count_cards())
print(d.pick())
print("score: ", d.count_cards())
print(d.pick())
print("score: ", d.count_cards())
