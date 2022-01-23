import random
randno = random.randint(1, 10)
userguess = None
guesses = 0
print('''\t\t*****************
\t\tGuessing Game:
\t\tGuess a number from 1 to 10 and you have only 3 tries. 
\t\tOtherwise you lose!

\t\t*****************\n''')
while(userguess != randno):
    if(guesses < 3):
        userguess = int(input("\t\tEnter your guess: "))
        guesses += 1
        if(userguess == randno):
            if(guesses == 1):
                # If user gets it right in first guess, Singular.
                print(f"\t\tYou guessed it  right in your {guesses}st try!")
            else:
                # If user gets it right in more than one guess, Pllural
                print(f"\t\tYou guessed it  right in {guesses} tries!")

        else:
            if(userguess > randno):
                print("\t\tYou guessed it wrong! Enter a smaller number")
            else:
                print("\t\tYou guessed it wrong! Enter a larger number")
    else:
        print(f"\n\t\tWRONG! Out of Tries!! . It was {randno}")
        break
