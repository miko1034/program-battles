from blockinit import createblock

blockList = []

for i in range(0,4):
    blockList.append(createblock("john"+str(i+1)))

while True:
    print(f"current health of {blockList[0][0]} is {blockList[0][1]}")
    if input("a") == "a":
        #finish later
        print(f" health of {blockList[0][0]} changed from {blockList[0][1]} to ")