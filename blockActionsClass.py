import random

def regenhealth(blockinfoList):
    health = blockinfoList[1]
    pluspercentage = f"1.0{random.randint(3,20)}"
    finalhealth = health * float(pluspercentage)
    blockinfoList[1] = health
    return health