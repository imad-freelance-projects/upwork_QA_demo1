class Ninja:
    def __init__(self) -> None:
        self.name= "ikem"
    
    @property
    def make(self):
        print("Hello worlds")
        
p = Ninja()

p.make