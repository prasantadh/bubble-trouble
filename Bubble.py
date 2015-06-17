class Bubble():
    def __init__(self, game, r):
        self.game = game
        self.r = r
        self.x = self.r + 50 ## 50 is the initial offset
        self.y = self.game.g - self.jumpHeight(r) 
        self.vx = 2
        self.vy = 1
    
    def jumpHeight(self, r):
        return ( 100 * (r//10) ) ## The height of shooter is hard-coded. adjust this later !error alert
    
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
        stroke(255)
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
