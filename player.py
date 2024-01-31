class Player:
    def __init__(self, name, char):
        self.name = name
        self.char = char
        self.score = 0
        
    def set_name(self, newName):
        self.name = newName
        
    def add_score(self):
        self.score = self.score + 1
    
    