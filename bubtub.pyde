from Shooter import Shooter as Shooter
from Bubble import Bubble as Bubble

class Game():
    def __init__(self, w, h, g):
        self.w = w
        self.h = h 
        self.g = g
    
    def display(self):
        stroke(255)
        line(0, game.g, self.w, self.g)    
        
game = Game(600,500,400)
shooter = Shooter(game, 20, 30)
bubble0 = Bubble(game, 40)
bubble1 = Bubble(game, 20)
bubble2 = Bubble(game, 10)
    
def setup():
    background(0)
    size(game.w, game.h)

def draw():
    background(0)
    game.display()
    shooter.display()
    bubble0.display()
    bubble1.display()
    bubble2.display()

def keyPressed():
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = True
    
def keyReleased():
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = False
    
    
    
        
