from Arrow import Arrow as Arrow

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
            self.v = -3
        elif self.controls[RIGHT]:
            self.v = 3
        elif self.controls[32]:
            if self.arrow == None:
                self.arrow = Arrow(self.game, self.x)
        else:
            self.v = 0
        
        #reset the arrow for shooter once the arrow reaches top
        ## also needs to reset the arrow once it hits the balloon. do it later.        
        if  self.arrow != None and self.game.g - self.arrow.l < 0:
            self.arrow = None
        
        self.x += self.v
        
        ## prevent the shooter going out of screen on left and right        
        if self.x - self.w < 0:
            self.x = self.w
        if self.x + self.w > self.game.w:
            self.x = self.game.w - self.w 
        
    def display(self):
        print(self.arrow)
        if self.arrow != None:
            self.arrow.display()
        self.update()
        stroke(255)
        fill(255,0,0)
        ellipse(self.x, self.y, 2*self.w, 2*self.h)
