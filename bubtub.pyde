from Shooter import Shooter as Shooter
from Bubble import Bubble as Bubble

class Game():
    def __init__(self, w, h, g, initBub):
        self.w = w
        self.h = h 
        self.g = g
        self.state = "Menu"
        self.initBub = initBub
        self.bubbles = []
        for j in range(initBub):
            self.bubbles.append(Bubble(self, 10, 90 * (j+1), 100, 1+j, 1)) 
        self.img =  loadImage("megaman.jpg")
        self.img2 = loadImage("ground.png")
        self.img_menu = loadImage("menu.png")
        self.img_gameover = loadImage("gameover.png")
        self.font = loadFont("PressStart2P-14.vlw")
    
    def update(self):
        temp =  []
        if shooter.arrow != None and shooter.hitsBubble():
            if self.victory():
                print("Congratulations!")
                self.initBub += 1
                self.__init__(900, 600, 500, game.initBub)
                self.state = "Playing"
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
              
game = Game(900,600,500, 1)
shooterWidth = 20
shooterHeight = 30
shooter = Shooter(game, shooterWidth, shooterHeight)
    
def setup():
    background(0)
    size(game.w, game.h)
    frameRate(50)

def draw():
    if game.state == "Menu":
        background(game.img_menu)
        textFont(game.font)
        fill(0)
        stroke(255, 255, 255)
        textSize(14)
        fill(255)
        text("Enter your name: ", 165, 275)
        fill(255)
        text(shooter.name, 245-4.7*len(shooter.name), 305)
        
        
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
        background(game.img_gameover)

def keyPressed():
    if game.state == "Playing":
        if keyCode in shooter.controls:
            shooter.controls[keyCode] = True
    elif game.state == "Menu":
        if keyCode == 8:
            shooter.name = shooter.name[:len(shooter.name)-1]
        elif keyCode == 10:
            game.state = "Playing"
        elif len(shooter.name) <= 10:
            shooter.name += str(key)
    
    
def keyReleased():
    if keyCode in shooter.controls:
        shooter.controls[keyCode] = False

def mouseClicked():
    if game.state == "Over":
        game.state = "Menu"
        game.__init__(game.w, game.h, game.g, 1)
        shooter.__init__(game, shooterWidth, shooterHeight, shooter.name)
    
    
    
    
        
