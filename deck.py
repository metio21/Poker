import random

class Card:
    """
    A class representing a single playing card with a suit and rank.
    """

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, suit, rank):
        """
        Initializes a Card with the given suit and rank.
        Raises a ValueError if the suit or rank is invalid.
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        Checks if two cards have the same rank.
        Used for comparisons like card1 == card2.
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compares two cards by rank.
        Returns True if self has a higher rank than other.
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        Returns a string representation of the card, e.g., "A♠" or "10♦".
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Returns the official string representation of the card (same as __str__).
        Used when printing a list of cards.
        """
        return self.__str__()

    @property
    def suit(self):
        """
        Returns the suit of the card.
        """
        return self._suit

    @property
    def rank(self):
        """
        Returns the rank of the card.
        """
        return self._rank

class Deck:
    """
    A class representing a standard 52-card deck.
    """

    def __init__(self):
        """
        Initializes the deck with all 52 unique cards.
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        Returns a string representation of the entire deck.
        Useful for debugging or printing all cards.
        """
        return str(self._deck)

    def shuffle(self):
        """
        Shuffles the deck randomly using the random module.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deals (removes and returns) the top card from the deck.
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    # Create a new deck
    deck = Deck()
    print(deck)  # Print deck before shuffling

    # Shuffle the deck
    deck.shuffle()
    print(deck)  # Print shuffled deck

    # Deal one card from the top
    print(deck.deal())  # Print the dealt card
