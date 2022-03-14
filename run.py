import random
import pyfiglet

menu_options = {
    "s": "Start",
    "r": "Restart",
    "e": "Exit",
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
        
        if game_choice == "s":
            break
        elif game_choice == "r":
            print("Restarting...")
        elif game_choice == "e":
            quit()
            print("Bye bye!")
        
        else:
            print("Invalid input, please choose from : s, r, e.")


def add_name():
    """
    Asks for player name and explain the game.
    """
    name = input('To start please enter your name: ')
    print("\n")
    print(f"Welcome {name}!\n")
    print("Can you solve 10 random math problems without a calculator?\n")
    print("You will have 5 seconds for each problems.\n")
    print(f"Good luck!\n")

def game():
    """
    The actual game function.
    Provides 10 random math calculations.
    When correct answer is given it adds one to the score.
    """
    questions = {}
    score = 0
    for i in range(10):
        int_x = random.randint(0,10)
        int_y = random.randint(0,10)
        operators = ["+", "-", "*"]
        operator_value = random.choice(operators)
        question = str(int_x)+" "+ str(operator_value)+ " "+str(int_y)
        answer = eval(question)
        question+=" = "
        
        questions.update({question:str(answer)})


    for q in questions.keys():
        user_answer = input(q)
        if questions.get(q) == str(user_answer):
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect! The answer was {answer}")
    print(f"You got {score}/10")
    game_menu()


def main():
    """
    Run all program functions
    """
    game_menu()
    add_name()
    game()

print(pyfiglet.figlet_format("Math Quiz", justify="center"))
main()