import time
import random

items = []

monsters = ["Ogar", "Dragon", "Troll", "Giant"]


def print_pause(message):
    print(message)
    time.sleep(1)


def restart_game():
    print_pause("Excellent! Restarting the game ...\n")
    items.clear()
    play_game()


# This is the message section for first point of entry and messages
# once user selects 1 or 2
def main_selection():
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2.)")


def first_selection_message(monster):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out "
                f"steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    # print_pause("You feel a bit under-prepared for this, what with "
    #             "only having a tiny dagger.")
    print_pause("Would you like to (1) fight or (2) run away?")


def second_selection_message():
    # print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take "
                "the sword with you.")
    print_pause("You walk back out to the field.")


# This portion of the code is the entry point of the code after the main
# selection of 1 or 2
def first_selection(monster):
    first_selection_message(monster)
    selection = gather_input_value()
    if selection == '1':
        if 'sword' in items:
            print_pause(f"As the {monster} moves to attack, you unsheath "
                        "your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand "
                        "as you brace yourself for the attack.")
            print_pause(f"But the {monster} takes one look at your shiny "
                        "new toy and runs away!")
            print_pause(f"You have rid the town of the {monster}. "
                        "You are victorious!")
        else:
            print_pause("You feel a bit under-prepared for this, what with "
                        "only having a tiny dagger.")
            print_pause("You do your best...")
            print_pause(f"but your dager is no match for the {monster}.")
            print_pause("You have been defeated!")
        selection = input("Would you like to play again? (y/n)")
        if selection == 'y':
            restart_game()
        else:
            print_pause("Thank you for playing rockstar!")
            print_pause("have a great day!")
            exit(0)
    elif selection == '2':
        print_pause("You run back into the field. Luckily, you don't seem "
                    "to have been followed.")
        main_selection()
        selection_action(monster)
    else:
        print_pause("Invalid selection!")
        print_pause("Please enter 1 or 2.")
        first_selection(monster)


def second_selection(monster):
    print_pause("You peer cautiously into the cave.")
    if 'sword' in items:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now")
        print_pause("You walk back out to the field.")
        main_selection()
        selection_action(monster)
    else:
        second_selection_message()
        items.append('sword')
        main_selection()
        selection_action(monster)


def monster_selection():
    return random.choice(monsters)


def gather_input_value():
    selection = input()
    return selection


# This is the main selection. The first time a player will be asked to make
# a selection.
def selection_action(monster):
    selection = gather_input_value()
    if selection == '1':
        first_selection(monster)
    elif selection == '2':
        second_selection(monster)
    else:
        print_pause("Invalid selection!")
        print_pause("Please enter 1 or 2.")
        selection_action(monster)


# The is the first message the player will receive when they start the game.
def intro():
    monster = monster_selection()
    # weapon = weapon_selection()
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")
    main_selection()
    return monster


def play_game():
    selection_action(intro())


play_game()
