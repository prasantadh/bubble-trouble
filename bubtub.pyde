from Shooter import Shooter as Shooter
from Bubble import Bubble as Bubble

class Game():
    def __init__(self, w, h, g):
        self.w = w
        self.h = h 
        self.g = g
        self.bubbles = []
        self.bubbles.append(Bubble(self, 20, 90, 100, 1, 1)) 
    
    def update(self):
        temp =  []
        if shooter.arrow != None and shooter.hitsBubble():
            if self.victory():
                print("Congratulations!")
        elif self.dead():
            print("Oops! you died!")
        else:
            pass
        
    def victory(self):
        print(self.bubbles)
        if self.bubbles == []:
            return True
        return False
    
    def dead(self):
        for bubble in self.bubbles:
            print(bubble.x + bubble.r, shooter.x - shooter.w)
#             print((bubble.x + bubble.r > shooter.x - shooter.w or bubble.x - bubble.r < shooter.x + shooter.w) and bubble.y + bubble.r > game.g - shooter.h)
            if (bubble.x + bubble.r > shooter.x - shooter.w and bubble.x - bubble.r < shooter.x + shooter.w) and (bubble.y + bubble.r > game.g - shooter.h):
                return True 
        return False
    
    def over(self):
        if self.victory() or self.dead():
            return True
        return False
        
    
    def display(self):
        #background(0)
        stroke(255)
        line(0, game.g, self.w, self.g)    
bgc = 0       
game = Game(900,600,500)
shooter = Shooter(game, 20, 30)
    
def setup():
    background(0)
    size(game.w, game.h)
    frameRate(50)

def draw():
    background(bgc)
    game.display()
    shooter.display()
    for bubble in game.bubbles:
        bubble.display()

def keyPressed():
#     print(keyCode, type(keyCode))
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = True
    
def keyReleased():
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = False
    
    
    
        
