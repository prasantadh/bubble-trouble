class Arrow():
    def __init__(self, game, x, startHeight):
        self.game = game
        self.x = x
        self.y = self.game.g
        self.l =  startHeight 
    
    def update(self):
        self.l += 10
    
    def display(self):
        self.update()
        stroke(255)
        line(self.x, self.game.g, self.x, self.game.g  - self.l)  
    
