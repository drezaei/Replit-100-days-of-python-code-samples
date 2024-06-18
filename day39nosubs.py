import os
import random

list_of_words = [
   "Abaddon", "Archon", "Bloodlust", "Cathedral", "Daemonic", "Dreadnought", "Eldritch", "Emperor",
    "Forgeworld", "Grimdark", "Hydra", "Inquisitor", "Javelins", "Kraken", "Liche",
    "Castellan", "Magician", "Necromancer", "Ogre", "Patriarch", "Phoenix", "Plaguebearer",
    "Realmstone", "Runecaster", "Skaven", "Slaughter", "Space", "Mechanicus", "Squig", "Baneblade", "Summoner",
    "Tomb", "Kings", "Troll", "Tyrant", "Ulric", "Vampire", "Vermintide", "Warphammer", "Witch", "Hunter",
    "Wyrm", "Aelf", "Altdorf", "Beastman", "Blackstone", "Bretonnia", "Dwarf", "Chosen",
    "Draconis", "Dwarfhold", "Empire", "Estalia", "Everchosen", "Giantslayer", "Greenskin", "Halberd",
    "Kislev", "Knightly", "Lichemaster", "Marienburg", "Norsca", "Maneater", "Ork", "Waaagh", "Paladin",
    "Phoenix", "Guard", "Pistolero", "Reiksguard", "Arbites", "Sieges", "Giant", "Sigmarite", "Slayer", "Sorcerer",
    "Tank", "Sylvania", "Templehof", "Trollblood", "Unseen", "Undead", "Elf", "Harlequins",
    "Wyrdstone", "Sororitas", "Ambull", "Astartes", "Battlewagon", "Beastmen", "Herd", "Orcs", "Blightbringer",
    "Bretonnians", "Knights", "Catacombs", "Spawn", "Eldar", "Dragons", "Engineer", "Count",
    "Gothic", "Giants", "Grimnir", "Grombrindal", "Halflings", "Dawi", "Hydrablood", "Chariot",
    "Jotunnheim", "Khaine", "Lizardmen", "Lothern", "Magik", "Nuln", "Militia", "Necromunda", "Kingdoms",
    "Necrons", "Pistolero", "Outlaws", "Realms", "Chaos", "Reiksland", "Slaangor", "Lasgun", "Sylvaneth",
    "Sigmar", "Trollslayers", "Horde", "Bloodlines", "Captain", "Cherubs",
    "Wraithlord"
]

word = random.choice(list_of_words).lower()
guesses = set()
lives = 0

def display_word():
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print("")

os.system("cls")
print("HANGMAN: WARHAMMER EDITION!")
print()
print("NO SUBROUTINE EDITION")

while True:
    diff = input("Select your difficulty:\n\n'H' for Hard Mode (4 lives)\n'N' for Normal Mode (6 lives)\n'E' for Easy Mode (12 lives)\n\n")

    if diff.lower() == "h" or diff.lower() == "hard":
        lives = 4
        break
    elif diff.lower() == "n" or diff.lower() == "normal":
        lives = 6
        break
    elif diff.lower() == "e" or diff.lower() == "easy":
        lives = 12
        break
    else:
        print("Invalid input, try again.")

input(f"You have {lives} lives to use.\nPress Enter to continue... ")
os.system("cls")

while lives > 0 and set(word) != guesses:
    display_word()

    guess = input(f"{lives} remaining. Guess a letter: ").lower()

    if guess in guesses:
        input("You already guessed that letter.")
        os.system("cls")
    elif guess in word:
        guesses.add(guess)
        input("Good guess!")
        os.system("cls")
    else:
        lives -= 1
        input(f"Incorrect. You have {lives} attempts left.")
        os.system("cls")

if set(word) == guesses:
    display_word()
    print(f"Congratulations! You guessed the word: {word}, with {lives} attempts remaining.")
else:
    print("😹LOOK @ THIS LOSER😹")
