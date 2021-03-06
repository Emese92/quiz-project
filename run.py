import random
from datetime import datetime
import pyfiglet
from termcolor import cprint
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Math_quiz_scoreboard')


menu_options = {
    1: "Start",
    2: "Instructions",
    3: "Exit",
}

MAX_QUESTIONS = 10

player_name = "User"


def show_instructions():

    """
    Gives instructions how to play the game.
    """
    print("Instructions\n")
    print("In this quiz, you are going to get ten random questions.")
    print("These are all basic mathematical problems.")
    print("You can mostly answer with a whole number.")
    print("When the answer is not a whole number, ")
    print("round up to 1 or 2 decimal places to get the correct answer.")
    print("e.g. 1.5, 3.33")
    print("At the end of the game your score will be automatically ")
    print("uploaded to a scoreboard.\n")


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
    Asks for a player name.
    """
    global player_name
    while True:
        name = input('To start please enter your name: \n')
        player_name = name
        if len(name) > 0:
            print("\n")
            print(f"Welcome {name}!\n")
            print("Can you solve 10 random math problems ")
            print("without a calculator?\n")
            print("Good luck!\n")
            break
        else:
            print("Please enter a valid name!")


def show_game_over_message(score):
    """
    Adds a message to the end of the game
    with the score number the player reached.
    """
    cprint(f"You got {score}/10", "blue")
    if score > 9:
        cprint("Congatulations!\n", "blue")
        cprint("You got it all right!\n", "blue")
    elif score >= 5 and score <= 9:
        cprint("You were very close!\n", "blue")
    else:
        cprint("Try harder next time.\n", "blue")


def update_scoreboard(score):
    """
    Uploads name, score and date to the scoreboard.
    """
    scoreboard = SHEET.worksheet("scoreboard")

    now = datetime.now()
    date = now.strftime("%x %H:%M:%S")

    scoreboard.append_row([player_name, score, date])


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
        # Used float() for the divisions that evaluate to floating point nums
        # Used round() so the whole numbers doesn't need .00
        question += " = "

        questions.update({question: str(answer)})
    return questions


def start_game():
    """
    The actual game function.
    When a correct answer is given it adds one to the score.
    It raises a Value error if not a number is given as an answer.
    CREDIT: Code inspired by a YouTube video:
    https://www.youtube.com/watch?v=h4n_ByFuD90
    """
    questions = generate_random_questions()
    score = 0

    for question in questions.keys():
        while True:
            try:
                user_answer = round(float(input(question)), 2)
                break
            except ValueError:
                print("This was not a number! Please enter your answer again!")

        if questions.get(question) == str(user_answer):
            score += 1
            cprint("Correct!\n", "green")
        else:
            cprint("Incorrect!\n", "red")

    update_scoreboard(score)
    show_game_over_message(score)
    show_game_menu()


def show_welcome_message():
    """
    Prints out a colored title formatted with pyfiglet.
    """
    cprint(pyfiglet.figlet_format("Math Quiz", justify="center"), "blue")


def main():
    """
    Run title and start menu functions
    """
    show_welcome_message()
    ask_user_name()
    show_game_menu()


main()
