from time import *
#Momin Javed and Antares Rahman
#Assignment 5
#Due: 9:30pm on Nov.8

#assignment.py

from buttonClass import *
from blackjackClass import *
import webbrowser

def anime(gwin): #draws the initial animation/program introduction
    gwin.setBackground("black")
    
    for i in range(6):
        im = Image(Point(85.7+(85.7*i),390), "playingcards/b1fv.gif")
        im.draw(gwin)
    for i in range(7):
        im = Image(Point(75+(75*i),490), "playingcards/b1fv.gif")
        im.draw(gwin)

    prompt = Text(Point(300,565), "Feeling lucky? Click to check it out!")
    prompt.setStyle("bold")
    prompt.setSize(15)
    prompt.setFill("white")
    prompt.draw(gwin)
                    
    gwin.getMouse()


    im = Image(Point(300,167.5), "Jokers/joker.gif")
    im.draw(gwin)

    sleep(0.5)

    for i in range(6):
        im = Image(Point(85.7+(85.7*i),390), "Jokers/j" + str(i+1) + ".gif")
        im.draw(gwin)
        sleep(0.13)
    for i in range(7):
        im = Image(Point(75+(75*i),490), "Jokers/j" + str(i+7) + ".gif")
        im.draw(gwin)
        sleep(0.13)

    #rules button drawn and activated
    rulesButton = Button(gwin, Point(42.5, 15), 85, 30, "Rules")
    rulesButton.activate()

    prompt.setSize(15)
    prompt.setText("Blackjack!\nClick 'Rules' for game rules or click anywhere else to begin.")

    pt = gwin.getMouse()

    if rulesButton.clicked(pt): #if 'Rules' is clicked, an online link explaining blackjack rules opens up
        webbrowser.open('http://www.blackjack-primer.com/basic_rules.php')
        rulesButton.deactivate()
        prompt.setSize(15)
        prompt.setText("Click anywhere to begin the Blackjack game!")
        gwin.getMouse()


def main():

    #GUI created and introduction/animation function called
    win = GraphWin("BlackJack",600, 600)
    anime(win)
    
    #background and buttons are drawn
    background = Image(Point(300,300), "casino.gif")
    background.draw(win)
    hit = Button(win, Point(150,250), 85, 30, "Hit")
    stand = Button(win, Point(450,250), 85, 30, "Stand")
    quitButton = Button(win, Point(300,570), 85, 30, "Quit")
    dealButton = Button(win, Point(300, 520), 85, 30, "Deal")
    rulesButton = Button(win, Point(42.5, 15), 85, 30, "Rules")

    #hit and stand button initially deactivated
    #quit, deal and rules button are activated
    hit.deactivate()
    stand.deactivate()
    quitButton.activate()
    dealButton.activate()
    rulesButton.activate()

    intro = Text(Point(300, 450), "Click 'Deal' each time you want to start \
a new deal!")
    intro.setFill("white")
    intro.setStyle("bold")
    intro.setSize(16) 
    intro.draw(win)
    
    pt = win.getMouse()
    while not quitButton.clicked(pt): #while quit button is not clicked
        if dealButton.clicked(pt): #if deal button is clicked

            #background and buttons re-drawn and activated/deactivated accordingly
            background = Image(Point(300,300), "casino.gif")
            background.draw(win)
            hit = Button(win, Point(150,250), 85, 30, "Hit")
            stand = Button(win, Point(450,250), 85, 30, "Stand")
            quitButton = Button(win, Point(300,570), 85, 30, "Quit")
            dealButton = Button(win, Point(300, 520), 85, 30, "Deal")
            rulesButton = Button(win, Point(42.5, 15), 85, 30, "Rules")
            hit.activate()
            stand.activate()
            quitButton.deactivate()
            dealButton.deactivate()
            rulesButton.activate()

            
            #display Text object setup, initially displaying nothing
            output = ""
            color = "black"
            display = Text(Point(300, 450), output)
            display.draw(win)
    
            BJ = BlackJack() #Deck created, and shuffled
            BJ.initDeal(win, 200,150, 200,350) #initial deal is initiated

            #both hands are evaluated and stored in variables
            dTotal = BJ.evaluateHand(BJ.getDHand()) #dealer's total
            pTotal = BJ.evaluateHand(BJ.getPHand()) #player's total
            
            dLabel = Text(Point(100, 140), "Dealer") #label "Dealer" drawn
            dTotLabel = Text(Point(100,160), "") #dealer's total is kept hidden

            pLabel = Text(Point(100, 340), "Player") #label "Player" drawn
            pTotLabel = Text(Point(100,360), "Total: "+str(pTotal)) #player's total is displayed

            dLabel.setStyle("bold")
            dTotLabel.setStyle("bold")
            pLabel.setStyle("bold")
            pTotLabel.setStyle("bold")
            dLabel.draw(win)
            dTotLabel.draw(win)
            pLabel.draw(win)
            pTotLabel.draw(win)
            
            pt = win.getMouse()
            off = 0 #offset setup for preventing hit cards from overlaping
            while not (dealButton.clicked(pt) or quitButton.clicked(pt)): #while deal or quit are not clicked
                if hit.clicked(pt):
                    BJ.hit(win, 280+off,350) #hit card drawn with offsetted x position
                    pTotal = BJ.evaluateHand(BJ.getPHand())
                    pTotLabel.setText("Total: " + str(pTotal)) #updated player total displayed
                    off = off + 40 #offset incremented
                    if pTotal > 21: #if player busts
                        #dealer's hidden card revealed by redrawing the first two cards from the dealer's hand
                        for j in range (2):
                            im = Image(Point(200+(40*j),150), "playingcards/" + BJ.getDHand()[j].getSuit()\
                                   + str(BJ.getDHand()[j].getRank()) + ".gif")
                            im.draw(win)
                            
                        #output is reset to display the current result
                        output = "You busted. Dealer wins!" 
                        color = "red4"
                        dTotLabel.setText("Total: " + str(dTotal))
                        hit.deactivate()
                        stand.deactivate()
                        quitButton.activate()
                        dealButton.activate()
                        
                elif stand.clicked(pt): #if stand is clicked
                    #dealer's hidden card revealed by redrawing the first two cards from the dealer's hand
                    for j in range (2):
                        im = Image(Point(200+(40*j),150), "playingcards/" + BJ.getDHand()[j].getSuit()\
                               + str(BJ.getDHand()[j].getRank()) + ".gif")
                        im.draw(win)
                        
                    BJ.dealerPlays(win, 280, 150) #dealer deals till soft 17 is reached
                    dTotal = BJ.evaluateHand(BJ.getDHand())
                    dTotLabel.setText("Total: " + str(dTotal))
                    
                    #dealer's total is evaluated and judged using if statements
                    #output is reset to display the result achieved
                    if dTotal > 21:
                        output = "Dealer busted. You win!"
                        color = "white"
                       
                    elif dTotal > pTotal:
                        output = "Dealer's total is "+str(dTotal)+" while your total \
is "+str(pTotal)+".\nDealer wins!"
                        color = "red4"
                                    
                    elif dTotal < pTotal:
                        output = "Dealer's total is "+str(dTotal)+" while your total \
is "+str(pTotal)+".\nYou win!"
                        color = "white"
                               
                    else:
                        output = "Nobody wins. It's a push!"
                        color = "white"
                 
                    hit.deactivate()
                    stand.deactivate()
                    quitButton.activate()
                    dealButton.activate()
                    
                elif rulesButton.clicked(pt): #online rules link opens if 'Rules' is clicked
                    webbrowser.open('http://www.blackjack-primer.com/basic_rules.php')

                #the output is drawn
                display.setText(output)
                display.setFill(color)
                display.setStyle("bold")
                display.setSize(17) 

                pt = win.getMouse()

        elif rulesButton.clicked(pt): #online rules link opens if 'Rules' is clicked
            webbrowser.open('http://www.blackjack-primer.com/basic_rules.php')
            pt = win.getMouse()
        
        else:
            pt = win.getMouse()
                
    win.close()
main()
