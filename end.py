class end:
    def __init__(self):
        self.age = 30
        self.name = "ikem"

    @property
    def say(self):
        return 3+3


p = end()
print(p.say)
