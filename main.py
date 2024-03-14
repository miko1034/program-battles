from block import Block
from func import makeMultipleBlocks, main

BLOCK_COUNT = 2

blocks = makeMultipleBlocks(BLOCK_COUNT)
for i in range(len(blocks)):
    blocks[i].changename(f"Block {i}")
    print(blocks[i].name, blocks[i].health)

main()