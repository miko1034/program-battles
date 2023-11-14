class blockInit:
    def __init__(self,name):
        self.name = name
        self.health = health


def multipleblockcreation(count):
    list = []
    for i in range(count):
        block = blockInit(f"block{i}",100)
        list.append(block)
    return list
=======
        self.health = 100
