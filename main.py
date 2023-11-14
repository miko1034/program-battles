from block import Block
from blockinit import blockInit
from func import multipleblockcreation

blocks = multipleblockcreation(3)
for i in range(len(blocks)):
    print(blocks[i].name, blocks[i].health)


if __name__ == "__main__":
    pass

#
#           COMPLETELY IGNORE THIS FILE UNTIL ALL THE BLOCK PROPERTIES
#           AND ACTIONS ARE COMPLETELY FINISHED!!!!!!!!!
#