from Shooter import Shooter as Shooter
from Bubble import Bubble as Bubble

class Game():
    def __init__(self, w, h, g):
        self.w = w
        self.h = h 
        self.g = g
        self.state = "Menu"
        self.bubbles = []
        self.bubbles.append(Bubble(self, 40, 90, 100, 1, 1)) 
        self.img =  loadImage("megaman.jpg")
        self.img2 = loadImage("ground.png")
    
    def update(self):
        temp =  []
        if shooter.arrow != None and shooter.hitsBubble():
            if self.victory():
                print("Congratulations!")
        elif self.dead():
            print("Oops! you died!")
            game.state = "Over"
        
    def victory(self):
        if self.bubbles == []:
            return True
        return False
    
    def dead(self):
        for bubble in self.bubbles:
            if (bubble.y + bubble.r > game.g - 2 * shooter.h) and (bubble.x + bubble.r > shooter.x - shooter.w and bubble.x - bubble.r < shooter.x + shooter.w):
                return True 
        return False
    
    ## this piece of code is not doing anything at all.
    def over(self):
        if self.victory() or self.dead():
            game.state = "Over"
            return True
        return False
        
    
    def display(self):
        stroke(255)
        line(0, game.g, self.w, self.g)
        image(self.img, 0, 0, game.w, game.h)
        image(self.img2,0, game.g, game.w, game.h - game.g)    
              
game = Game(900,600,500)
shooterWidth = 20
shooterHeight = 30
shooter = Shooter(game, shooterWidth, shooterHeight)
    
def setup():
    background(0)
    size(game.w, game.h)
    frameRate(50)

def draw():
    if game.state == "Menu":
        background(255, 0, 0)
        textSize(24)
        fill(0)
        text("Enter your name: ", 50, 50)
        text(shooter.name, 250, 50)
        
    elif game.state == "Playing":
        background(0)
        game.update()
        game.display()
        fill(0,255,0)
        rect(shooter.x-shooter.w, game.g - 2 * shooter.h, 2 * shooter.w, 2 * shooter.h)
        shooter.display()
        for bubble in game.bubbles:
            bubble.display()
    else:
        background(0,255,0)

def keyPressed():
    if game.state == "Playing":
        if keyCode in shooter.controls:
            shooter.controls[keyCode] = True
    elif game.state == "Menu":
        if keyCode == 8:
            shooter.name = shooter.name[:len(shooter.name)-1]
        elif keyCode == 10:
            game.state = "Playing"
        else:
            shooter.name += str(key)
    
    
def keyReleased():
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = False

def mouseClicked():
    if game.state == "Over":
        game.state = "Menu"
        game.__init__(game.w, game.h, game.g)
        shooter.__init__(game, shooterWidth, shooterHeight, shooter.name)
    
    
    
    
        
