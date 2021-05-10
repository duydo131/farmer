from Animal import Animal


class Dog(Animal):
    def __init__(self):
        self.weight = 20
        self.dw = 5
        self.dh = 2
        self.wfat = 30
        self.dead = False
        self.dead_weight = 16

    def bark(self):
        return "meow meow meow"

    def hurry(self):
        self.weight -= self.dh
