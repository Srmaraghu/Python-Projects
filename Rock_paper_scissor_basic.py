import random


def gamewin(comp, you):
    if(you == comp):
        return 'tie'
    elif(you == 'r' and comp == 's') or (you == 's' and comp == 'p') or (you == 'p' and comp == 'r'):
        return True
    else:
        return False

while(True):
    print('''\n\t\t***************************************\n
    \t\tComputer's Turn: Rock(r), scissor(s) , paper(p).
    \t\tComputer has choosen.''')
    # randno = random.randint(1, 3)
    # if(randno == 1):
    #     comp = 'r'
    # elif(randno == 2):
    #     comp = 'p'
    # else:
    #     comp = 's'

    # All the steps commented out above is equal to the one line of code just down.
    comp = random.choice(['r', 'p', 's'])
    you = input("\t\tYour Turn: Rock(r), scissor(s) , paper(p): ")
    gamewin(comp, you)
    print("\n\t\tComputer Chose: ", comp)
    print("\n\t\tYou Chose: ", you)

    a = gamewin(comp, you)
    if(a == 'tie'):
        print("\n\t\tIt's a Tie!\n")
    elif(a == True):
        print("\n\t\tYou win!\n")
    elif(a == False):
        print("\n\t\tYou Lose!\n")
    
    ans=input("Do you want to continue (y/n)? : ").lower()
    if(ans=='n'):
        break
    elif(ans=='y'):
        True

    
print("\t\t\nThanks for playing.")



