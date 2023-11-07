from block import Block
from blockinit import blockinit

block1 = blockinit()
print(block1.health)
block1.changehealth(block1.health, 10)
print(block1.health)