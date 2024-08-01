#Dice simulator
import random

def roll_dice():
    num=random.randint(1,6)

    if num==1:
        print(' -------------')
        print('|             |')
        print('|      *      |')
        print('|             |')
        print(' -------------')

    elif num==2:
        print(' -------------')
        print('|             |')
        print('|   *     *   |')
        print('|             |')
        print(' -------------')   

    elif num==3:
        print(' -------------')
        print('|             |')
        print('|   *  *  *   |')
        print('|             |')
        print(' -------------')       

    elif num==4:
        print(' -------------')
        print('|   *     *   |')
        print('|             |')
        print('|   *     *   |')
        print(' -------------')   

    elif num==5:
        print(' -------------')
        print('|   *     *   |')
        print('|      *      |')
        print('|   *     *   |')
        print(' -------------')     

    elif num==6:
        print(' -------------')
        print('|   *     *   |')
        print('|   *     *   |')
        print('|   *     *   |')
        print(' -------------')   

print("!--------------Dice Simulator--------------!")
x ='y'
while x.lower()=='y':
    roll_dice()
    roll_again=input("Do you want to roll again(y/n):") #user have to select 'y' to roll again & 'n' to exit
    if roll_again.lower()=='n':
        exit(0)

