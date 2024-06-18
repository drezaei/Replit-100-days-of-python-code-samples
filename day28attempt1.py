import random, os, time

def die():
    roll6 = random.randint(1, 6)
    roll12 = random.randint(1, 12)
    return roll6, roll12

def die6():
    roll6 = random.randint(1,6)
    return roll6

def stats():
    roll6, roll12 = die()
    health = int((roll6 * roll12) / 2) + 10
    strength = int((roll6 * roll12) / 2) + 12
    print("Health: " + str(health))
    print("Strength: " + str(strength))
    return health, strength

def character_generator():
    name =input("What is your first character's name?       ")
    title =input("What is your first character's title?     ")
    adj =input("What adjective best describes your first character?     ")
    car =input("What is your first character's class or career?     ")
    print("")
    character = title + " " + name + " " + "the" + " " + adj + " " + car
    print("Welcome to the fight,", character)
    hp, stre = stats()
    return name, title, adj, car, character, hp, stre

def character_generator1():
    print("")
    name1 =input("What is your second character's name?     ")
    title1 =input("What is your second character's title?       ")
    adj1 =input("What adjective best describes your second character?       ")
    car1 =input("What is your second character's class or career?       ")
    print("")
    character1 = title1 + " " + name1 + " " + "the" + " " + adj1 + " " + car1
    print("Good to see you,", character1)
    hp1, stre1 = stats()
    return name1, title1, adj1, car1, character1, hp1, stre1

def prefightHP(hp, hp1):
    print("")
    print("Before we begin, let's have a few seconds to assess our two combatants.")
    time.sleep(3)
    if hp > hp1:
        print(title1, name1, "is the peakier of the two, with " + title, name + " having", hp-hp1, "more hitpoints.")
    elif hp1 > hp:
        print(title, name, "is the peakier of the two, with " + title1, name1 + " having", hp1-hp, "more hitpoints.")
    else:
        print("Both characters have the same amount of health. Skill and luck will determine their fates.")

def prefightSTRE(stre, stre1):
    time.sleep(3)
    if stre > stre1:
        print("The " + adj, car, "will have less trouble overcoming his opponent's defences. The", adj1, car1 + " scores", stre-stre1, "points less on offence." )
    elif stre1 > stre:
        print("The " + adj1, car1, "will have less trouble overcoming his opponent's defences. The", adj, car + " scores", stre1-stre, "points less on offence." )
    else:
        print("An equal measure of skill. Fortitude and luck will decide the victor.")

def fightHYPE():
    time.sleep(3)
    print("")
    print("So without further ado, LETS GET READY TO RUMBLE!!!!!!")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

def clears():
    os.system('cls')

def rounds(character, character1, hp, hp1, title, title1, name, name1, stre, stre1):
    round = 1
    while True:
        chaRoll = die6()  # Assuming die6 is defined somewhere in your code
        cha1Roll = die6()  # Assuming die6 is defined somewhere in your code
        ChaDamaged = int(hp - ((stre1 - stre) + 1))
        Cha1Damaged = int(hp1 - ((stre - stre1) + 1))

        print()
        print(character)
        print("Health:", hp)
        print()
        print(character1)
        print("Health:", hp1)
        print()
        

        if chaRoll > cha1Roll:
            hp1 -= Cha1Damaged
            print(f"Round: {round}, {title} {name} has damaged {title1} {name1}.")
            time.sleep(5)
            os.system("cls")
        elif chaRoll < cha1Roll:
            hp -= ChaDamaged
            print(f"Round: {round}, {title1} {name1} dealt a blow to {title} {name}.")
            time.sleep(5)
            os.system("cls")          
        else:
            print(f"Round: {round}: the unstoppable force met the unmovable object, with no result either way.")
            time.sleep(5)
            os.system("cls")
            
        if hp <= 0:
            winner = character1
            print(f"{title} {name} has fainted!")
            print(f"It took {round} rounds, but eventually {character1} won the day!")
            break
        elif hp1 <= 0:
            winner = character
            print(f"{title1} {name1} went crying back to mummy!")
            print(f"{character} was the champion of that fight, in only {round} rounds!")
            break
        else:
            print("")
            round += 1


   
print("WELCOME TO THE ARENA!")
print("")
print("Two characters meet, only one of them leaves.... ALIVE!")
print("Let's begin by creating your first champion.")


name, title, adj, car, character, hp, stre = character_generator()
name1, title1, adj1, car1, character1, hp1, stre1 = character_generator1()
roll6 = die6
prefightHP(hp, hp1)
prefightSTRE(stre, stre1)
fightHYPE()
clears()
rounds(character, character1, hp, hp1, title, title1, name, name1, stre1, stre)