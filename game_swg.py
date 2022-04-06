import random 
import sys
def gameWin(Comp, You):
    if Comp == You:
        return None

    elif Comp == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True

    elif Comp == 'w':
        if You == 'g':
            return False
    elif You == 's':
            return True

    elif Comp == 'g':
        if You == 's':
            return False
        elif You == 'w':
            return True
print("Comp Turn: Snake(s) Water(w) Gun(g) ? : ")
randNo = random.randint(1, 3)
if randNo == 1:
    Comp = 's'
elif randNo == 2:
        Comp = 'w'
elif randNo == 3:
        Comp = 'g'

You = input("Your Turn: Snake(s) Water(w) Gun(g) ? : ")

a = gameWin(Comp, You)

print(f"Computer Chose {Comp}")
print(f"You chose {You}")

if a == None:
    print("The game is tie !")

elif a:
    print("You Win !")
else:
    print("You Lose !")
