
class Game():
    def __init__(self, w, h, g):
        self.w = w
        self.h = h 
        self.g = g
    
    def display(self):
        stroke(255)
        line(0, game.g, self.w, self.g)
        
class Shooter():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.x = game.w/2
        self.y = game.g-self.h
        self.v = 0
        self.controls = {LEFT : False, RIGHT : False, 32 : False} #32 is for detecting the spacebar pressed and released
        
    def update(self):
        print(self.controls[LEFT])
        if self.controls[LEFT]:
            self.v = -3
        elif self.controls[RIGHT]:
            self.v = 3
        else:
            self.v = 0
        
        self.x += self.v
        
        ## prevent the shooter going out of screen on left and right        
        if self.x - self.w < 0:
            self.x = self.w
        if self.x + self.w > game.w:
            self.x = game.w - self.w 
        
    def display(self):
        self.update()
        stroke(255)
        ellipse(self.x, self.y, 2*self.w, 2*self.h)


class Balloon():
    def __init__(self, r):
        self.r = r
        self.x = self.r + 50 ## 50 is the initial offset
        self.y = game.g - self.jump(r) 
    
    def jump(self, r):
        return 10*r
    
    def display(self):
        stroke(255)
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
    
        
game = Game(600,500,400)
shooter = Shooter(20, 30)
balloon = Balloon(10)
    
def setup():
    background(0)
    size(game.w, game.h)

def draw():
    background(0)
    game.display()
    shooter.display()
    balloon.display()

def keyPressed():
    print(keyCode)
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = True
    
def keyReleased():
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = False
    
    
    
        
