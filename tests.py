from blockActionsClass import blockActions
from blockinit import blockInit

#creation of block1
block1 = blockInit("block1", 100)

#init
actions = blockActions(block1.name,block1.health)

#print basic info of block1
print(block1.name)
print(block1.health)