from blockinit import createblock

blockList = []

for i in range(0,4):
    blockList.append(createblock("john"+str(i+1)))


print(blockList)