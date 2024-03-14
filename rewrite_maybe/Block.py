import random

class Block:
    def __init__(self,name="",size=1,state=True):
        self.name = name
        self.health = random.randint(70,100)
        self.size = size
        self.state = state

    def setname(self, newname):
        self.name = newname

    def attack(self,targetBlock):
        chanceToDealDamage = 30
        num = random.randint(0,100)
        if num > 30:
            print("attack Failed")
            pass
        else:
            damage = -random.randint(5,15)
            if (targetBlock.health - damage) > 0:
                targetBlock.health += damage
                print(damage)
            else:
                targetBlock.state = False
                print("Block is dead")
                
    