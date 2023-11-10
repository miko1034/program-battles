import random

class Block:
    def __init__(self, health):
        self.health = health

    def changehealth(self,currenthealth, desiredchange):
        self.health = int(currenthealth) + int(desiredchange)
        return str(self.health)

def blockinit():
    starthealth = f"{random.randint(75,100)}"
    block = Block(starthealth)
    return block

