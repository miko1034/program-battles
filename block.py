import random

class Block:
    def __init__(self, name=""):
        self.health = random.randint(70,100)
        self.name = name

    def changehealth(self,desiredchange):
        self.health += desiredchange
        return self.health

    def changename(self,somename):
        self.name = somename 