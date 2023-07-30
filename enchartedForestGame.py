import re
import random

player_name = ""
player_inventory = []
forest_locations = ["Clearing", "Cave", "River", "Bridge", "Thicket"]

re_move = re.compile(r"(go|move) (to )?(?P<location>\w+)")
re_look_around = re.compile(r"(look around|explore|search)")
re_talk_to = re.compile(r"(talk to|speak to) (?P<character>\w+)")
re_take_them = re.compile(r"(take|pick up) (?P<item>\w+)")
re_inventory = re.compile(r"(inventory|items)")

characters = {
    "elf": "Greetings, brave traveler! What brings you to the Enchanted Forest?",
    "dwarf": "Ho there! Watch your step, lad. The forest can be treacherous.",
    "fairy": "Welcome to the mystical forest! Would you like some fairy dust?",
}

def main():
    global player_name
    print("Welcome to the Enchanted Forest")
    player_name = input("What is your name, adventurer? ")
    intro()
    game_loop()


def intro():
    print(f"Hello, {player_name}! You find yourself at the edge of the Enchanted Forest.")
    print("Your goal is to explore the forest.")

def game_loop():
    while True:
        print(
            "\n go or move to <location>",
            ", ".join(forest_locations),
            "\n look around or explore or search",
            "\n talk to or speak to <character>",
            ", ".join(characters),
            "\n take or pick up <item>",
            "\n inventory or items",
            "\n exit or quit"
        )
        player_input = input("\nWhat would you like to do? ").lower()


        if player_input == "exit".lower() or player_input == "quit".lower():
            print("Farewell, brave adventurer! See you again!")
            break
        elif re_move.match(player_input):
            move_player(player_input)
        elif re_look_around.match(player_input):
            explore()
        elif re_talk_to.match(player_input):
            talk_to_character(player_input)
        elif re_take_them.match(player_input):
            take_item(player_input)
        elif re_inventory.match(player_input):
            show_inventory()
        else:
            print("I don't understand. Try Again!")

def move_player(player_input):
    location_match = re_move.match(player_input)
    location = location_match.group("location").capitalize()

    if location in forest_locations:
        print(f"You move to the {location}")
    else:
        print("You can't go there.")
def explore():
    print(f"You are in the {random.choice(forest_locations)}.")
    if random.randint(1, 3) == 1:
        encounter_character()
def encounter_character():
    character = random.choice(list(characters.keys()))
    print(f"A {character} appears before you.")
    print(characters[character])
def talk_to_character(player_input):
    character_match = re_talk_to.match(player_input)
    character = character_match.group("character").lower()
    if character in characters:
        print(characters[character])
    else:
        print("There is no one with that name here.")

def take_item(player_input):
    item_match = re_take_them.match(player_input)
    item = item_match.group("item").lower()
    print(f"You pick up the {item}.")
    player_inventory.append(item)

def show_inventory():
    if player_inventory:
        print("You are carrying: ")
        for item in player_inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")

if __name__ == "__main__":
    main()













































