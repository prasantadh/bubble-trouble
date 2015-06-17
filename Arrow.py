class Arrow():
    def __init__(self, game, x):
        self.game = game
        self.x = x
        self.y = self.game.g
        self.l =  30 ## l for length, hardcoded height of the shooter
    
    def update(self):
        self.l += 5
    
    def display(self):
        self.update()
        stroke(255)
        line(self.x, self.game.g, self.x, self.game.g  - self.l)  
    
