import random

dice = random.randint(1, 6)
while True :
    if dice == 6:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("dice is 6, dice1= ",dice1,"dice2=",dice2)
        break
    
    if 1 <= dice <= 5 :
        print("dice is ", dice)
        break