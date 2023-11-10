from block import Block,blockinit
from func import attack

block1 = blockinit()
block2 = blockinit()

print(f"block1 health is {block1.health}")
block1.changehealth(block1.health, 10)
print(f"block1 now is {block1.health}")

print(f"block2 health is {block2.health}")
block2.changehealth(block2.health, -10)
print(f"block2 now is {block2.health}")
