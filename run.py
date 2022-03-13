import random
import pyfiglet

menu_options = {
    's': 'Start',
    'r': 'Restart',
    'e': 'Exit',
}

def game_menu():
    """
    Displays menu options for the player to choose from.
    """
    for key in menu_options.keys():
        print('Press -', key, '- to -', menu_options[key])
    while True:
        print("\n")
        game_choice = input("What would you like to do? \n")
        
        if game_choice == "s":
            break
        elif game_choice == "r":
            restart_game()
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

  


def main():
    """
    Run all program functions
    """
    game_menu()
    add_name()

print(pyfiglet.figlet_format("Math Quiz", justify="center"))
main()