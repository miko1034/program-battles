import random
from blockinit import blockInit

class blockActions:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def attack(self, target):
        pass

    def gethealth(self):
        return self.health()
    
    def defend(self):
        pass

    def disengage(self):
        pass

    def regenhealth(self,health):
        pluspercentage = f"1.0{random.randint(3,20)}"
        finalhealth = health * float(pluspercentage)
        return round(finalhealth)
    #doenst work yet
    #pls try fix asap
    #this is just a testing thingy btw (like a debug/dev tool)
    def applydamage(self,damage,health):
        newhealth = round(health - damage)
        return newhealth
        