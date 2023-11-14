from block import Block

#block = Block(0)

def multipleblockcreation(count):
    list = []
    for i in range(count):
        block = blockInit(f"block{i}",100)
        list.append(block)
    return list

#def attack(target,damage):
#    block = Block(target)
#    block.changehealth(block.health, damage)
#    return block.health

    #work on this next pls :)
#
#           COMPLETELY IGNORE THIS FILE UNTIL ALL THE BLOCK PROPERTIES
#           AND ACTIONS ARE COMPLETELY FINISHED!!!!!!!!!
#