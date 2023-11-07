import random
from block import Block

def blockinit():
    starthealth = f"{random.randint(79,100)}"
    block = Block(starthealth)
    return block
