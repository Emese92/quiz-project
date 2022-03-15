import random
import pyfiglet

from termcolor import cprint


menu_options = {
    1: "Start",
    2: "Instructions",
    3: "Exit",
}

def show_instructions():
    """
    Gives instructions to play the game.
    """
    print("Instructions\n")
    print(" ")


def show_game_menu():
    """
    Displays menu options for the player to choose from.
    """
    for key in menu_options.keys():
        print("Press -", key, "- to -", menu_options[key])
    while True:
        print("\n")
        game_choice = input("What would you like to do? \n")       
        if game_choice == "1":
            return start_game()
        elif game_choice == "2":
            show_instructions()
            return show_game_menu()
        elif game_choice == "3":
            print("Bye bye!")
            quit()
        else:
            print("Invalid input, please choose from : 1, 2, 3")


def ask_user_name():
    """
    Asks for a valid player name.
    """
    name = input('To start please enter your name: ')
    print("\n")
    print(f"Welcome {name}!\n")
    print("Can you solve 10 random math problems without a calculator?\n")
    print("Good luck!\n")


def start_game():
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
            cprint("Correct!\n", "green")
        else:
            cprint("Incorrect!\n", "red")
            

    print(f"You got {score}/10\n")
    show_game_menu()

def show_welcome_message():
    """
    Prints out a colored title formatted with pyfiglet.
    """
    cprint(pyfiglet.figlet_format("Math Quiz", justify="center"), "blue")


def main():  
    """
    Run all program functions
    """
    show_welcome_message()
    ask_user_name()
    show_game_menu()


main()
