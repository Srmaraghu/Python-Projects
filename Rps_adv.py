from csv import excel
import random
import time


def game_instructions():
    print()
    print("Instructions for Rock, Paper, Scissors: ")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()


def the_game_code():
    while(True):
        print("---------------------")
        print("Enter \"help\" for instructions.")
        print("Enter \"r for Rock\",\"p for Paper\",\"s for Scissor\" to play.")
        print("Enter \"back\" to go the main menu.")
        print("Enter \"exit\" to end the game.")

        print("--------------------")
        print()

        you = input("Enter your move: ").lower()

        if(you == 'help'):
            game_instructions()
            continue
        elif you == 'exit':
            print("\n\tThanks for playing!!!!")

            exit()
        elif you == 'back':
            break
        elif(you == 'r'):
            player_move = 0
        elif(you == 'p'):
            player_move = 1
        elif(you == 's'):
            player_move = 2
        else:
            print("\tWrong Input .")
            time.sleep(.5)

            game_instructions()
            continue

        print("\nComputer making its move.....")
        print()
        time.sleep(2)
        comp = random.randint(0, 2)
        print(f"Computer choose: ", game_map[comp].upper())

        winner = rps_table[player_move][comp]

        if winner == player_move:
            print(name, "WINS!!!")
        elif winner == comp:
            print("COMPUTER WINS!!!")
        else:
            print("TIE GAME")

        print()
        time.sleep(2)


if __name__ == "__main__":
    game_map = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "Spock"}
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
    name = input("Enter your name: ")

    while True:
        print()
        print("Let's Play!!!")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to quit")
        print()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please Enter the Correct Input.")
            continue
        if choice == 1:
            the_game_code()
        elif choice == 2:
            print("\n\tThanks for playing!!!!")
            break
        else:
            print("Wrong Input. Read Instructions Carefully !")
