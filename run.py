import random
import pyfiglet
from termcolor import cprint


menu_options = {
    1: "Start",
    2: "Instructions",
    3: "Exit",
}

MAX_QUESTIONS = 10


def show_instructions():

    """
    Gives instructions how to play the game.
    """
    print("Instructions\n")
    print("In this quiz you are going to get 10 random questions.")
    print("These are all basic mathematical problems.")
    print("You can mostly answer with a whole number.")
    print("When the answer is not a whole number, ")
    print("use 1 or 2 decimal places to get the correct answer.")
    print("e.g. 1.5, 3.33,")


def show_game_menu():
    """
    Displays menu options for the player to choose from.
    """
    print("+--------------------------------+")
    for key in menu_options.keys():
        print("   Press -", key, "- to -", menu_options[key])
    print("+--------------------------------+")
     
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
    while True:
        name = input('To start please enter your name: ')
        if len(name) > 4:
            print("\n")
            print(f"Welcome {name}!\n")
            print("Can you solve 10 random math problems without a calculator?\n")
            print("Good luck!\n")
            break
        else:
            print("Please enter a valid name")


def show_game_over_message(score):
    """
    Adds a message to the end of the game
    with the score number the player reached.
    """
    cprint(f"You got {score}/10", "blue")
    if score > 9:
        cprint("Congatulations!\n", "blue")
        cprint("You got it all right!\n", "blue")
    elif score > 5 and score < 9:
        cprint("You were very close!\n", "blue")
    else:
        cprint("Try harder next time\n", "blue")


def generate_random_questions():
    """
    Provides 10 random math calculations.
    """
    questions = {}

    for _ in range(MAX_QUESTIONS): 
        int_x = random.randint(5, 10)
        int_y = random.randint(1, 5)
        operators = ["+", "-", "*", "/"]
        operator_value = random.choice(operators)
        question = str(int_x)+" " + str(operator_value) + " "+str(int_y)
        answer = round(float(eval(question)), 2)
        question += " = "

        questions.update({question: str(answer)})
    return questions
    

def start_game():
    """
    The actual game function.
    When correct answer is given it adds one to the score.
    CREDIT: Code inspired by a YouTube video:
    https://www.youtube.com/watch?v=h4n_ByFuD90
    """
    questions = generate_random_questions()
    score = 0
    
    for q in questions.keys():
        while True:
            try:
                user_answer = round(float(input(q)), 2)
                break
            except ValueError:
                print("This was not a number! Please enter your answer again!")

        if questions.get(q) == str(user_answer):
            score += 1
            cprint("Correct!\n", "green")
        else:
            cprint("Incorrect!\n", "red")

    show_game_over_message(score)
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
