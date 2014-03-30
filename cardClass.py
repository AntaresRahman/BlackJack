class Card:

    """A Card is an object with a specific rank and belongs to a
    suit (Spades, Clubs, Hearts, Diamonds)."""

    def __init__(self, rank, suit):

        """Creates a Card object with a rank and a suit."""
        self.cardRank = rank
        self.cardSuit = suit
        self.rankList = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.suits = {"s":"Spades", "c": "Clubs", "h": "Hearts", "d": "Diamonds"}

    def getRank(self):
        """Returns the rank value of the card."""
        return self.cardRank

    def getSuit(self):
        """Returns the initial of the suit to which the card belongs."""
        return self.cardSuit

    def BJValue(self):
        """Returns the value of the card, when used in Blackjack."""
        value = self.cardRank
        if value > 10:
            value = 10
        return value

    def __str__(self):
        """When prompted to print the Card object, this method prints
        out the card info, displaying its rank and suit.
        e.g.
        print(Card(1,s)) will print ---> Ace of Spades."""
        return (self.rankList[self.cardRank-1]+" of "+self.suits[self.cardSuit]+".")
    
    
