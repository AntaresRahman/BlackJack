from deckClass import *
from graphics import *

class BlackJack:

    """Works using a Deck object and performs various methods on the deck,
    used during a blackjack game."""

    def __init__(self):

        """This creates a Deck of 52 cards in a list and shuffles them randomly."""
        self.cardDeck = Deck() #a Deck object created containing 52 cards
        self.cardDeck.shuffle() #the Deck gets a shuffle
        self.hand_d = [] #this is the dealer's hand, which is set to be an empty list
        self.hand_p = [] #this is the player's hand, which is set to be an empty list
        
    def initDeal(self, gwin, xposD, yposD, xposP, yposP):

        """This method appends the dealer's hand and the player's hand with two
        cards each and draws them at dealer coordinates(xposD, yposD) and player
        coordinates (xposP, yposP). However, a face-down card is drawn instead of the
        first dealer card and the card x positions are offsetted to overcome overlap."""
        for i in range (2): #two cards given to each hand
            self.hand_p.append(self.cardDeck.dealCard()) #top card from the deck given to the player
            im = Image(Point(xposP+(40*i),yposP), "playingcards/" + self.hand_p[-1].getSuit()\
                       + str(self.hand_p[-1].getRank()) + ".gif")
            im.draw(gwin) #the same card drawn on the player's part of the GUI

            self.hand_d.append(self.cardDeck.dealCard()) #top card from the deck given to the dealer
            if i == 0:
                im = Image(Point(xposD+(40*i),yposD), "playingcards/b1fv.gif") #face-down card drawn at the first instance
            else:
                im = Image(Point(xposD+(40*i),yposD), "playingcards/" + self.hand_d[-1].getSuit()\
                       + str(self.hand_d[-1].getRank()) + ".gif")
            im.draw(gwin) #actual card dealt, drawn at the second instance

    def hit(self,gwin, xpos, ypos):
        """Appends and draws the top card from the Deck to the player's hand at position
        (xpos, ypos)."""
        self.hand_p.append(self.cardDeck.dealCard()) #top card from the deck appended to the player's hand
        im = Image(Point(xpos, ypos), "playingcards/" + self.hand_p[-1].getSuit()\
                       + str(self.hand_p[-1].getRank()) + ".gif")
        im.draw(gwin)

    def evaluateHand(self, hand):
        """Totals and returns the value of the hand passed to the method. If hand contains an Ace, Ace is counted
        as 11 if allowing so does not make the total go over 21. Otherwise Ace is counted as 1.""" 
        total = 0
        hasAce = False #boolean flag setup to check presence of Ace in hand
        for card in hand:
            if card.BJValue() == 1:
                hasAce = True #if Ace is present, boolean flag turned True
            total = total + card.BJValue()

        if hasAce and total+10 <= 21: #if Ace is present, and counting Ace as 11
                                      #does not make the player/dealer bust, Ace
                                      #is counted as 11. Else, Ace counted as 1.
            total = total + 10

        return total

    def dealerPlays(self, gwin, xPos, yPos):
        """Appends and draws cards to the dealer's hand in gwin till he/she reaches soft or hard 17. Card images
        drawn start from position (xPos, yPos) and are offsetted each time."""
        dTotal = self.evaluateHand(self.hand_d) #dealer's hand is totalled and stored in dTotal
        offset = 0 #offset setup to prevent overlaping
        while dTotal < 17: #while dealer's hand is less than 17, new cards appended and drawn at offsetted positions
            self.hand_d.append(self.cardDeck.dealCard())
            im = Image(Point(xPos+offset,yPos), "playingcards/" + self.hand_d[-1].getSuit()\
                       + str(self.hand_d[-1].getRank()) + ".gif")
            im.draw(gwin)
            offset = offset + 40
            dTotal = self.evaluateHand(self.hand_d)

    def getDHand(self):
        """Returns the dealer's hand in the form of a list."""
        return self.hand_d

    def getPHand(self):
        """Returns the player's hand in the form of a list."""
        return self.hand_p
