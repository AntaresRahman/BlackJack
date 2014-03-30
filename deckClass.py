from cardClass import *
from random import *

class Deck:

    """A Deck object consists of a deck of 52 different cards."""

    def __init__(self):
        """Creates a list of 52 different Card objects, with unique
        rank-suit combinations. Increments the card counter by one
        each time a new card is added to the card list."""
        self.cardList = [] #an initial list of cards is setup
        self.totCards = 0 #total number of cards in the list
        
        for s in ["d", "c", "h", "s"]: #initials represent card suits
            for r in range (1,14): #represents card ranks from 1 to 13
                                   #1:Ace, 11:Jack, 12:Queen, 13:King
                
                self.cardList.append(Card(r,s))
                self.totCards = self.totCards + 1 #number of cards in the list
                                                  #incremented each time a new
                                                  #card appended
         
    def shuffle(self):
        """Shuffles the list of 52 cards created, by randomly appending
        cards to a shuffle list and setting it equal to the card list
        at the end."""
        shuffleList = [] #an empty shuffle list is setup
        for i in range (len(self.cardList)):

            #random card from the card list popped out each time
            randCard = self.cardList.pop(randrange(len(self.cardList)))

            #random card appended to the shuffle list
            shuffleList.append(randCard)    
        self.cardList = shuffleList #shuffle list made into the new card list


    def dealCard(self):
        """Returns and pops out the first card from the card list, and
        decreases the card counter by one."""
        self.totCards = self.totCards - 1
        return(self.cardList.pop(0))

    def cardsLeft(self):
        """Returns the total number of cards remaining in the list."""
        return self.totCards
        
                
        
                
