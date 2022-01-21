import random
low = 1
high = 10
guesses = 0
feedback = ''
print('''\t\t********************************\n
\t\tThe player have to imagine a number in his/her mind and the computer tries to match the number it generated to the player's. 
\t\tIf the number is high, player enters 'h' 
\t\tElse if number is low, player enters 'l'
\t\tand if the number matches the player's imagination number, Computer Wins!!\n
\t\t********************************''')
while feedback != 'c':
    if(guesses < 3):
        comp_guess = random.randint(low, high)
        guesses += 1
        feedback = input(
            f"\t\tIs {comp_guess} too high(H), low(L) or correct(c)?:  ")

        if feedback == 'h':
            high = comp_guess-1
        elif feedback == 'l':
            low = comp_guess+1
    else:
        print("\t\tComputer couldn't guess the number.\n")
        exit()

if(guesses==1):
    print(f"\n\t\tThe Computer guessed it right in its {guesses}st try.\n")
else:
    print(f"\n\t\tThe Computer guessed it right in {guesses} tries.\n")
    