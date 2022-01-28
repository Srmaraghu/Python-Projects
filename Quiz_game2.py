import random
class QA:
    def __init__(self, question, correct_answer, other_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.other_answer = other_answer

def new_game():
    question_answer_list = [QA("Who created Python?", " Guido van Rossum", [" Elon Musk", " Bill Gates", " Mark Zuckerburg"]),
                            QA("What year was Python created?",
                            " 1991", [" 1989", " 2000", " 2016"]),
                            QA("Python is tributed to which comedy group? ",
                            " Monty Python", [" Lonely Island", " Smosh", " SNL"]),
                            QA("Is the Earth round? ", " True", [" False", " sometimes", " What's Earth?"])]

    correct_answers_count = 0
    random.shuffle(question_answer_list)

    for items in question_answer_list:
        print(items.question)
        # As other answers are already in a list, we are adding the correct answer in the list as well.
        options_of_ques = items.other_answer+[items.correct_answer]

        random.shuffle(options_of_ques)

        count = 0
        while count < len(options_of_ques):
            print(f"{count+1} : {options_of_ques[count]}")  # displaying options
            count += 1



        while(True):
            try:
                userguess = int(input('\nEnter the corresponding option number : '))
                if(userguess > len(options_of_ques)  or userguess==0):
                    print("\nThis doesn't correspond to any option. Please enter a valid option.\n")
                    continue

                elif (options_of_ques[userguess-1] == items.correct_answer):
                    print("\nCorrect!\n")
                    correct_answers_count += 1
                    break

                else:
                    print(f"\nYour answer was wrong!! Correct answer was {items.correct_answer}\n")
                    print()
                    break
            except ValueError as e:
                    print("\nPlease Enter a valid Integer!\n")
                    continue

    print(f"\nYou scored {correct_answers_count} out of {str(len(question_answer_list))}.")

def play_again():
    response=input("Do you want to play again? (y/n) : ").upper()

    if(response=="Y"):
        return True
    else:
        return False

if __name__=="__main__":
    new_game()
    while(play_again()):
        new_game()

