import random
from words import word_list
from hang import hang
import string
import time
#extract a random word from  words.py
def word_selected():
    secret_word=random.choice(word_list).upper()
    while '-'  in secret_word or ' ' in secret_word:
        secret_word=random.choice(word_list).upper()
    
    return(secret_word)
 
def hangman():
    while(True):
        errors=0
        lives=7
        
        play_again=True
        secret_word=word_selected()
        # print(secret_word)
        letters_in_word=set(secret_word) #stores the letters that are inside our secret word
        # print (letters_in_word)
        alphabet=set(string.ascii_uppercase) #storing the Capital letters of english alphabets in a set.
        # print (alphabet)
        guessed_letters=set() # used to store the letters in the word user will guess .
        while len(letters_in_word)>0 and errors<7:
            #To display the letters used by player
            time.sleep(0.65)
            print("==========================================================================================================\n")
            print("\n\t\tYou have used these letters: ",','.join(guessed_letters))
            print(f"\t\tYou have {lives}❤️  left.")
            #ASKING user for the guess

            word_list=[letter if letter in guessed_letters else '-' for letter in secret_word ] #this statement either fills the screen with  dashes(-) for user to guess or letters user has guessed.
            print("\t\tGuess The Word : ",' '.join(word_list) )
            guess=input("\n\t\tEnter your guess: ").upper()

            if guess in alphabet -  guessed_letters:
                guessed_letters.add(guess)
                if guess in  letters_in_word:
                    time.sleep(0.25)

                    print("\n\t\tThat was a correct guess.")
                    print("==========================================================================================================\n")


                    letters_in_word.remove(guess)

                else:
                    time.sleep(0.25)
                    print(f"\n\t\tOops! '{guess}' isn't in the word.")
                    time.sleep(0.5)
                    print(hang[errors])
                    errors+=1
                    lives-=1
                    print("==========================================================================================================\n")


            
            elif guess in guessed_letters:
                print(f"\n\t\tYou have already tried the letter \'{guess}\'. Try another letter.")
            
            else:
                print("\n\t\tInvalid character. Please type a valid input.")

    
        if errors ==7:
            print(f"\n\t\t You died. the Word was {secret_word}.")
        else:
            print(f"\n\t\tYou won!. The word was {secret_word} indeed.")

        print("\n---------------------------------------------------------------------------------------------------------------------------")
        print()   
        
        play_again=input("Do you want to play again (y/n)? : ")
        if play_again=='y':
                True
        elif play_again=='n':
            break
        else:
            print("Enter either y or n.")





hangman()