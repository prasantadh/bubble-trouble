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
        self.controls = {LEFT : False, RIGHT : False, 32 : False} #32 is for detecting the spacebar pressed and released
    
    def display(self):
        stroke(255)
        ellipse(self.x, self.y, 2*self.w, 2*self.h)


class Balloon():
    def __init__(self):
        
        
game = Game(600,420,400)
shooter = Shooter(20, 30)
    
def setup():
    background(0)
    size(game.w, game.h)

def draw():
    game.display()
    shooter.display()

def keyPressed():
    print(keyCode)
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = True
    
def keyReleased():
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = False
    
    
    
        
