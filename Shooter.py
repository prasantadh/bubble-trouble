from Arrow import Arrow as Arrow
from Bubble import Bubble as Bubble

class Shooter():
    def __init__(self, game, w, h):
        self.game = game
        self.w = w
        self.h = h
        self.x = self.game.w/2
        self.y = self.game.g-self.h
        self.v = 0
        self.controls = {LEFT : False, RIGHT : False, 32 : False} #32 is for detecting the spacebar pressed and released
        self.arrow = None
        
    def update(self):
        if self.controls[LEFT]:
            self.v = -5
        elif self.controls[RIGHT]:
            self.v = 5
        else:
            self.v = 0
        if self.controls[32]:
            if self.arrow == None:
                self.arrow = Arrow(self.game, self.x)
        
        ## reset the arrow for shooter once the arrow reaches top
        ## also reset arrow once the bubble is hit. done in the game.update()        
        if  self.arrow != None and self.game.g - self.arrow.l < 0:
            self.arrow = None
        elif self.arrow  != None or (self.arrow == None and self.game.bubbles == []):
            self.game.update()
        else:
            pass
            
        
        self.x += self.v
        
        ## prevent the shooter going out of screen on left and right        
        if self.x - self.w < 0:
            self.x = self.w
        if self.x + self.w > self.game.w:
            self.x = self.game.w - self.w 
    def hitsBubble(self):
        output = False
        temp = []
        for index, bubble in enumerate(self.game.bubbles):
                ## if arrow hits the bubble
                if bubble.x - bubble.r < self.arrow.x < bubble.x + bubble.r and bubble.y + bubble.r > self.game.g - self.arrow.l:
                    output = True
                    ##print ("hit", self.arrow.x)
                    ## if it is the smallest bubble, remove it
                    if bubble.r != bubble.smallest:
                        bubble1 = Bubble(self.game, bubble.r/2, self.arrow.x-bubble.r/2, bubble.y, -1, -3)
                        bubble2 = Bubble(self.game, bubble.r/2, self.arrow.x+bubble.r/2, bubble.y, +1, -3)
                        temp = self.game.bubbles[:index] + [bubble1] + [bubble2] + self.game.bubbles[index+1:]
                    ## if it not the smallest bubble, split it
                    else:
                        ## print(self.bubbles, index)
                        self.game.bubbles.pop(index)
                    ## the arrow disappears
                    self.arrow = None
                    ## no more bubbles to check for that arrow
                    break
        if temp!= []:
            self.game.bubbles = [] + temp
        return output
        
        
        
    def display(self):
#         print(self.arrow)
        if self.arrow != None:
            self.arrow.display()
        self.update()
        stroke(255)
        fill(255,0,0)
        ellipse(self.x, self.y, 2*self.w, 2*self.h)
