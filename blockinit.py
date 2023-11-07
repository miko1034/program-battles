import random

def createblock(name):
    health = random.randint(50,100)
    theblock = [name,health]
    return theblock