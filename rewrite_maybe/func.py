from Block import Block


#creates a list, containing Block objects, with length count
def createblocks(count):
    blocklist = [Block() for i in range(count)]
    for i in range(len(blocklist)):
        blocklist[i].setname(f"Block{i+1}")
        print(blocklist[i].name, blocklist[i].health, blocklist[i].state)
    return blocklist