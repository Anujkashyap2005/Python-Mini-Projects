import random

'''
0 gun
1 snake
-1 water

'''
computer = random.choice([-1,0,1])

you = input("Enter your choice snake/gun/water: ")

youdict = {"snake":1, "gun":0, "water":-1}

reversedict = {1:"snake", 0:"gun",-1:"water"}

am = youdict[you]

print(f"Your choice {reversedict[am]}\ncomputer choice {reversedict[computer]}")


if(computer == am):
    print("match draw")

else:

    if(computer == 1 and am == 0):
        print("You win")
    
    elif(computer == 0 and am == 1):
        print("You loose!")

    elif(computer == -1 and am == 0):
        print("you win")
    
    elif(computer == 1 and am == -1):
        print("you loose!")
        
    elif(computer == 0 and am == -1):
        print("you win")

    elif(computer == -1 and am == 1):
        print("you loose!")
    else:
        print("Exit")