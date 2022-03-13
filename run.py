import random
import pyfiglet



def add_name():
    """
    Asks for player name and expain the game.
    """
    name = input('To start please enter your name: ')
    print(f"Welcome {name}!\n")
    print("Can you solve 10 random math problems without a calculator?\n")
    print("You will have 5 seconds for each problems.\n")
    print(f"Good luck!\n")

    


def main():
    """
    Run all program functions
    """
    add_name()

print(pyfiglet.figlet_format("Math Quiz", justify="center"))
main()