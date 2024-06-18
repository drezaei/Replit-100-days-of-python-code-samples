import os, random, time

character_1 = ()
character_1_health = 0
character_1_power = 0

def main_menu():
    global character_1, character_1_health, character_1_power

    while True:
        menu=int(input("1) Create Character\n2) See Character Sheet\n3) Reset Character\n"))

        if menu == 1:
            character_creator()
        elif menu == 2:
            if not character_1:
                input("You have no saved characters. Press enter to return to menu: ")
                os.system("cls")
            elif input(f"Name: {character_1}\nHealth: {character_1_health}\nPower: {character_1_power}"):
               time.sleep(3)
               os.system("cls")
        elif menu == 3:
            character_1 = ()
            character_1_health = ()
            character_1_power = ()
            input("Saved character deleted, press enter to continue.")
            os.system("cls")

def character_creator():
    global character_1

    os.system("cls")
    character_name=input("What is your first character's name:\n")
    character_title=input("What is your character's title:\n")
    character_profession=input("What is your character's profession or class\n")
    os.system("cls")
    character_1 = (f"{character_title} {character_name} the {character_profession}")
    input(f"Welcome to the fight, {character_1}!")
    character_stats()

def character_stats():
    global character_1, character_1_health, character_1_power

    os.system("cls")
    d6_roll, d12_roll = dice_roller()
    health = int (d6_roll * d12_roll) // 2 + 10
    power = int (d6_roll * d12_roll) // 2 + 12
    character_1_health = health
    character_1_power = power
    input(f"{character_1}\nHealth: {character_1_health}\nPower: {character_1_power}\nPress Enter to continue:  ")
    os.system("cls")


def dice_roller():
    d6_roll=random.randint(1,6)
    d12_roll=random.randint(1,12)
    return d6_roll, d12_roll


main_menu()