class Block:
    def __init__(self, health,name):
        self.health = health
        self.name = name

    def changehealth(self,currenthealth, desiredchange):
        self.health = int(currenthealth) + int(desiredchange)
        return str(self.health)

