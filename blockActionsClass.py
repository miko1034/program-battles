import random

class blockActions:
    def __init__(self):
        #,size,target,damage,health
#        self.size()
#        self.target()
#        self.damage()
#        self.health()
        pass
    def attack(self, target):

        pass
    def defend(self):
        pass
    def disengage(self):
        pass
    def regenhealth(self,health):
        pluspercentage = f"1.0{random.randint(3,20)}"
        finalhealth = health * float(pluspercentage)
        return round(finalhealth)