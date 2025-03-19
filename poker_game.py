from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):

        _cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = _cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    @property
    def is_Flush(self):
        for card in self.cards[1:0]:
            if card[0].suit != card.suit:
                return False
        return True

count = 0
flushes = 0
while flushes < 100:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand._flush:
        flushes += 1
    count += 1

print(f"probability of a flush is {100*flushes/count}%")




