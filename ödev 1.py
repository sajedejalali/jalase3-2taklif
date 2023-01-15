import random

name = input("what's your name?")
pc_number = random.randint(0 , 100)
num = 0
while True:
    user_number = int(input("enter number 0-100 : "))
    num += 1
    if pc_number == user_number :
       print(name, "you win!!! number = ", pc_number, "tries = ", num)
       break

    

    if pc_number < user_number :
        print("go down...")

    else :
        print("go up...")