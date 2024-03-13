from block import Block
from func import makeMultipleBlocks

blocks = makeMultipleBlocks(3)
for i in range(len(blocks)):
    blocks[i].setname(f"Block {i}")
    print(blocks[i].name, blocks[i].health)
