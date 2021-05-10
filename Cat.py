from Animal import Animal


class Cat(Animal):
    def __init__(self):
        self.weight = 10
        self.dw = 2
        self.dh = 1
        self.wfat = 13
        self.dead = False
        self.dead_weight = 8

    def bark(self):
        return "woof woof woof"
