import random
randno=random.randint(1,10)
userguess=None
guesses=0

while(userguess!=randno):
    if(guesses<3):
        userguess=int(input("Enter a number: "))
        guesses+=1 
        if(userguess==randno):
            print(f"You guessed it  right in {guesses} guesses!")
        else:
            if(userguess>randno):
                print("You guessed it wrong! Enter a smaller number")
            else:
                print("You guessed it wrong! Enter a larger number")
    else:
        print("You Guessesd it wrong\n Out of Tries!! You Lose!!")
        break



            

