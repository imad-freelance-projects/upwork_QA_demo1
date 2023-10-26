class detach:
    def __init__(self) -> None:
        print("say hello detach")

    @property
    def make(self):
        return "make"


d = detach()
print(d)