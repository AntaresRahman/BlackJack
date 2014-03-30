from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
   
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h

        #p1 and p2 form the two corners of our button
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = True #this variable keeps track of whether or not the button is currently "active"

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True          #boolean variable that tracks "active"-ness to True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False #boolean variable that tracks "active"-ness to False

    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        if self.active == True and self.xmin <= p.getX() <= self.xmax\
           and self.ymin <= p.getY() <= self.ymax:
            return True

    
def main():
    #creating a graphical window in which to test the Button class
    win = GraphWin()

    Roll = Button(win, Point(100,130), 70, 20, "Roll Dice")
    Quit = Button(win, Point(100,170), 70, 20, "Quit")
    Roll.activate()

    Quit.deactivate()
    
    pt = win.getMouse()
   
    #testing the clicked() boolean method...
    while not Quit.clicked(pt):
        if Roll.clicked(pt):
            Quit.activate()
        pt = win.getMouse()
        
    #we reach this line of code when quit button is clicked b/c loop condition breaks
    win.close() #so close the window, ending the program
    
if __name__ == "__main__":
    main()
