from deck import Deck, Card

class PokerHand:
    """
    A class that represents a poker hand (5 cards) and evaluates various hand types,
    such as flush, straight, full house, etc.
    """

    def __init__(self, deck):
        """
        Initializes a PokerHand by dealing 5 cards from the given deck.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Returns the list of cards in the hand.
        """
        return self._cards

    def __str__(self):
        """
        Returns a string representation of the hand (list of 5 cards).
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Checks if all cards in the hand have the same suit (i.e., a flush).
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        """
        Checks if the hand is a full house: 3 cards of one rank and 2 of another.
        In this simplified version, this occurs if number_matches == 8.
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        Counts the number of pairwise rank matches among the 5 cards.
        Returns:
            int: total number of matches.
            e.g., 1 pair → 2 matches, 2 pairs → 4 matches, trips → 6, full house → 8, quads → 12
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if the hand contains exactly one pair.
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        Checks if the hand contains two different pairs.
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        Checks if the hand contains three cards of the same rank (three of a kind).
        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        Checks if the hand contains four cards of the same rank (four of a kind).
        """
        return self.number_matches == 12

    @property
    def is_straight(self):
        """
        Checks if the hand contains 5 consecutive ranks (no duplicates).
        Assumes cards can be sorted based on rank index.
        """
        self.cards.sort()  # Uses Card.__gt__ to sort based on rank
        distance = Card.RANKS.index(self.cards[4].rank) - Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4


# Simulation to estimate the probability of getting a straight
count = 0       # Total number of hands dealt
matches = 0     # Number of hands that are straights

while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)

    if hand.is_straight:
        matches += 1
        print(hand)  # Print the hand that resulted in a straight

    count += 1

# Print estimated probability after observing 10 straights
print(f"Probability of a straight is {100 * matches / count}%")
