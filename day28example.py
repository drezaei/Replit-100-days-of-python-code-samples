import random, os, time

def die():
    roll6 = random.randint(1, 6)
    roll12 = random.randint(1, 12)
    return roll6, roll12

def stats():
    roll6, roll12 = die()
    health = int((roll6 * roll12) / 2) + 10
    strength = int((roll6 * roll12) / 2) + 12
    return health, strength

def commentHP(cha0HP, cha1HP, title0, name0, title1, name1, race1, class1):
    # ... (rest of the function remains unchanged)

def commentSTR(cha0STR, cha1STR, title1, name1, title0, name0, race0, class0):
    # ... (rest of the function remains unchanged)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fight():
    # ... (unchanged)

def round(cha0, cha0HP, cha0STR, cha1, cha1HP, cha1STR):
    clear()
    print("ROUND 1")
    # ... (rest of the function remains unchanged)

print("WELCOME TO THE ARENA!")
# ... (unchanged)

# Call stats for both characters before using their health values
cha0HP, cha0STR = stats()
cha1HP, cha1STR = stats()

commentHP(cha0HP, cha1HP, title0, name0, title1, name1, race1, class1)
commentSTR(cha0STR, cha1STR, title1, name1, title0, name0, race0, class0)
fight()
round(cha0, cha0HP, cha0STR, cha1, cha1HP, cha1STR)
