import random

class Block:
    def __init__(self, name="", stamina=5,size=1):
        self.health = random.randint(70,100)
        self.name = name
        self.stamina = stamina
        self.size = size

    def changehealth(self,desiredchange):
        self.health += desiredchange
        return self.health

    def changename(self,somename):
        self.name = somename 
    
    def attack(self,targetBlock):
        damage = targetBlock.changehealth(-random.randint(5,15))
        print(f"{self.name} attacked {targetBlock} and dealt {damage}")

    def defend(self):
        pass
    def grow(self):
        pass
    def heal(self):
        pass

    def doAction(self,action):
        if action == "attack":
            self.attack()
        elif action == "defend":
            self.defend()
        elif action == "grow":
            self.grow()
        elif action == "heal":
            self.heal()