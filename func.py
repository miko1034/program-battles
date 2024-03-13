from block import Block


def makeMultipleBlocks(count):
    mylist = [Block() for i in range(count)]
    return mylist