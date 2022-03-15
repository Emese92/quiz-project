import random
import pyfiglet
import colorama
from colorama import Fore, Back, Style


menu_options = {
    1: "Start",
    2: "Exit",
}


def game_menu():
    """
    Displays menu options for the player to choose from.
    """
    for key in menu_options.keys():
        print("Press -", key, "- to -", menu_options[key])
    while True:
        print("\n")
        game_choice = input("What would you like to do? \n")       
        if game_choice == "1":
            break
        elif game_choice == "2":
            print("Bye bye!")
            quit()
        else:
            print("Invalid input, please choose from : 1, 2.")


def add_name():
    """
    Asks for player name and explain the game.
    """
    name = input('To start please enter your name: ')
    print("\n")
    print(f"Welcome {name}!\n")
    print("Can you solve 10 random math problems without a calculator?\n")
    print("Good luck!\n")


def game():
    """
    The actual game function.
    Provides 10 random math calculations.
    When correct answer is given it adds one to the score.
    CREDIT: Code inspired by a YouTube video:
    https://www.youtube.com/watch?v=h4n_ByFuD90
    """
    questions = {}
    score = 0
    
    for i in range(10): 
        int_x = random.randint(5, 10)
        int_y = random.randint(1, 5)
        operators = ["+", "-", "*"]
        operator_value = random.choice(operators)
        question = str(int_x)+" " + str(operator_value) + " "+str(int_y)
        answer = eval(question)
        question += " = "

        questions.update({question: str(answer)})

    for q in questions.keys():
        while True:
            try:
                user_answer = int(input(q))
                break
            except ValueError:
                print("This was not a number!")

        
        if questions.get(q) == str(user_answer):
            score += 1
            print("\033[32m" + "Correct!\n")
            print('\033[39m')
        else:
            print("\033[31m" + "Incorrect!\n")
            print('\033[39m')

    print(f"You got {score}/10\n")
    main()

def main():  
    """
    Run all program functions
    """
    game_menu()
    add_name()
    game()

print(pyfiglet.figlet_format("Math Quiz", justify="center"))
main()
