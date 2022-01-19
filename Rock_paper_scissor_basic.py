import random


def gamewin(comp, you):
    if(you == comp):
        return None
    elif(comp == 'r'):
        if(you == 's'):
            return False
        if(you == 'p'):
            return True
    elif(comp == 'p'):
        if(you == 's'):
            return True

        if(you == 'r'):
            return False

    elif(comp == 's'):
        if(you == 'p'):
            return False
        if(you == 'r'):
            return True


randno = random.randint(1, 3)
comp = print("Computer's Turn: Rock(r), scissor(s) , paper(p): \n")
if(randno == 1):
    comp = 'r'
elif(randno == 2):
    comp = 'p'
else:
    comp = 's'

you = input("Your Turn: Rock(r), scissor(s) , paper(p): ")
gamewin(comp, you)
print("Computer Chose:", comp)
print("You Chose:", you)
a = gamewin(comp, you)
if(a == None):
    print("It's a Tie!")
elif(a == True):
    print("You win!")
elif(a == False):
    print("You Lose!")
