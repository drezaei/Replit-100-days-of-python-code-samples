import random, os, time

char1_name=""
char1_health=0
char1_power=0

char2_name=""
char2_health=0
char2_power=0

def main_menu():
    global char1_name, char1_health, char1_power, char2_name, char2_health, char2_power
    os.system("cls")
    while True:
        menu=int(input(f"1: Create characters\n2: View created chracters\n3: Fight! Fight! Fight!\n4: Delete characters\n5: Use default characters\n"))

        if menu == 1:
            character_creator()
        
        elif menu == 2:
            if not char1_name:
                os.system("cls")
                print("You have not generated any characters.")
                time.sleep(1.5)
                os.system("cls")

            else:
                os.system("cls") 
                input(f"{char1_name}\nHealth: {char1_health}\nPower: {char1_power}\n\n{char2_name}\nHealth: {char2_health}\nPower: {char2_power}\n\nPress Enter to return to menu.\n")
                os.system("cls")

        elif menu == 3:
            fight_fight_fight()

        elif menu == 4:
            os.system("cls")
            char1_name=()
            char1_health=0
            char1_power=0
            char2_name=()
            char2_health=0
            char2_power=0

            print("Characters deleted.")
            time.sleep(1.5)
            os.system("cls")

        elif menu == 5:
            os.system("cls")
            char1_name="Sir Abe the Lazy Knight"
            char1_health=72
            char1_power=6

            char2_name="Lord Bob the Stupid Wizard"
            char2_health=64
            char2_power=12

            print("Two characters created.")
            time.sleep(1.5)
            os.system("cls")
            


def character_creator():
    global char1_name, char1_health, char1_power, char2_name, char2_health, char2_power
    os.system("cls")

    char1_firstname=input("What is your first character's name:  ").title()
    char1_title=input(f"What is {char1_firstname} title:  ").title()
    char1_class=input(f"What is {char1_title} {char1_firstname}'s profession or class:  ").title()
    char1_adjective=input(f"What adjective best describes your {char1_class}:   ").title()
    char1_name = (f"{char1_title} {char1_firstname}, the {char1_adjective} {char1_class}")
    
    d6_roll, d12_roll = dice_roller()
    char1_health = int (d6_roll * d12_roll) // 2 + 10
    char1_power = int (d6_roll * d12_roll) // 2 + 12
    
    print()

    input(f"All arise for {char1_name}!\nHealth: {char1_health}\nPower: {char1_power}\n\nPress Enter to create a challenger for your character.")

    print()

    char2_firstname=input("What is your second character's name:  ").title()
    char2_title=input(f"What is {char2_firstname} title:  ").title()
    char2_class=input(f"What is {char2_title} {char2_firstname}'s profession or class:  ").title()
    char2_adjective=input(f"What adjective best describes your {char2_class}:   ").title()
    char2_name = (f"{char2_title} {char2_firstname}, the {char2_adjective} {char2_class}")
    
    d6_roll, d12_roll = dice_roller()
    char2_health = int (d6_roll * d12_roll) // 2 + 10
    char2_power = int (d6_roll * d12_roll) // 2 + 12

    print()

    question=input(f"Welcome to the fight, {char2_name}!\nHealth: {char2_health}\nPower: {char2_power}\n\nEnter 'yes' to immediately go to the fighting pits, anything else returns to menu.")
    
    if question.lower() in ["yes","y","ye"]:
        fight_fight_fight()

    else:
        main_menu()


def dice_roller():
    d6_roll=random.randint(1,6)
    d12_roll=random.randint(1,12)
    return d6_roll, d12_roll

def fight_fight_fight():

    if not char1_name:
        os.system("cls")
        print("You haven't even created any fighters, you numpty!")
        time.sleep(1.5)
        main_menu()
    
    else:
        print("\nAlright, before the fight, let's take a look at our combatants.\n")
        
        time.sleep(3)
        
        if char1_health > char2_health:
            print(f"Between the two combatants, {char1_name} is the heartier of the two, having {char1_health-char2_health} more health points.\n")
            time.sleep(1.5)
        
        else: print(f"{char2_name} can claim to being the healthier of the two fighters, with {char2_health-char1_health} more hit points.\n" ) 
        time.sleep(1.5) 

        if char1_power > char2_power:
            print(f"{char1_name} can deliver greater damage than their foe, with a higher power score.\n")
            time.sleep(1.5)

        else: print(f"{char2_name} can deliver greater damage than their foe, with a higher power score.\n")
        time.sleep(1.5)

        print("So without further ado, LETS GET READY TO RUMBLE!!!!!!")
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)

        time.sleep(1.5)

        os.system("cls")

        actual_fight_4_realz_now()

def actual_fight_4_realz_now():
    global char1_name, char1_health, char2_name, char2_health, char1_power, char2_power

    round = 1

    d6_roll = dice_roller()

    while char1_health > 0 and char2_health > 0:
        cha1_roll = dice_roller()
        cha2_roll = dice_roller()
        
        print(f"{char1_name}")
        print(f"Health: {char1_health}")
        print()
        print(f"{char2_name}")
        print(f"Health: {char2_health}")
        
        if cha1_roll > cha2_roll:
            round += 1
            damage = char1_power // 2
            char2_health -= damage
            print(f"\n{char1_name} lands a blow on {char2_name}, dealing {damage} points of damage!\n")
            time.sleep(1.5)
            os.system("cls")

        elif cha2_roll > cha1_roll:
            round += 1
            damage = char2_power // 2
            char1_health -= damage
            print(f"\n{char2_name} lands a blow on {char1_name}, dealing {damage} points of damage!\n")
            time.sleep(1.5)
            os.system("cls")

    if char1_health <= 0:
        print(f"{char1_name} wins the game in {round} rounds!")
        time.sleep(1.5)
        main_menu()
    
    elif char2_health <= 0:
        print(f"{char2_name} wins the game in {round} rounds!")
        time.sleep(4)
        main_menu()


main_menu()