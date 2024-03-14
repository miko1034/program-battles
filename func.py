from block import Block
import os

def makeMultipleBlocks(count):
    mylist = [Block() for i in range(count)]
    return mylist

def main():
    from main import blocks as blocklist
    #menu
    while True:
        os.system("clear")
        for i in range(len(blocklist)):
            print(blocklist[i].name, blocklist[i].health,blocklist[i].size)
        choice = int(input("\nWhat action do you want to do?\n1) Attack\n2) Grow\n3) Quit"))
        if choice == 1:
            blocklist[0].attack(blocklist[1])