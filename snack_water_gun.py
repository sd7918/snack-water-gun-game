import random

def gameWin(comp,you):
    if comp==you:
        return None
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

print("comp turm: Snake(s) Water(w) Gun(g)?")
randNo=random.randint(1, 3)
# print(randNo)
if randNo==1:
    comp='s'
elif(randNo==2):
    comp='g'
elif(randNo==3):
    comp='w'
you=input("your turm: Snake(s) Water(w) Gun(g)?")

a=gameWin(comp,you)
print(f"computer coose {comp}")
print(f"your choose {you}")
if a ==None:
    print("its a tie!")
elif a:
    print("you win")
else:
    print("You lose")




