class Animal:
    def bark(self):
        pass

    def eat(self):
        if(self.weight <= self.dead_weight):
            print("I'm a {class_name} and I'm so dead!".format(
                class_name=self.__class__.__name__))
            return
        self.weight += self.dw
        if(self.weight < self.wfat):
            print("Mlem mlem! I'm a {class_name} with weight {weight}, {bark}"
                  .format(class_name=self.__class__.__name__, weight=self.weight, bark=self.bark()))
        else:
            print("Mlom mlom! I'm a fat {class_name} with weight {weight}, {bark}"
                  .format(class_name=self.__class__.__name__, weight=self.weight, bark=self.bark()))

    def hurry(self):
        if(self.weight <= self.dead_weight):
            return
        self.weight -= self.dh

    def isFat(self):
        return self.weight >= self.wfat

    def isDead(self):
        return self.weight <= self.dead_weight

    def isNormal(self):
        return not(self.isDead() | self.isFat())
