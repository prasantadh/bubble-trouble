class Bubble():
    
    def __init__(self, game, r, x, y, vx, vy):
        self.game = game
        self.r = r
        self.x = x
        self.y = y 
        self.vx = 2 * vx
        self.vy = vy
        self.smallest = 10 
    
    def jumpHeight(self, r):
        return ( 100 * (r//10) - 30 * 0.2) ## The height of shooter is hard-coded. adjust this later !error alert
    
#     def isHit(self):
#         if 
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
    
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy+= 0.2
        
        if self.y + self.r > self.game.g:
            self.y = self.game.g - self.r
            self.vy = -1 * (self.r//10) - 30 * 0.2 ## (-1 * (self.r//10) + 30/0.2) ## another instance of hardcoding shooter height
        
        ## put the bubble within the game screen
        if self.x - self.r < 0:
            self.x = self.r
            self.vx *= -1
        if self.x + self.r > self.game.w:
            self.x = self.game.w - self.r 
            self.vx *= -1
    
    def display(self):
        self.update()
        self.game.update()
        stroke(255)
        fill(255)
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
