import os, random, time
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

word = random.choice(list_of_words)
word = word.lower()
correctGuesses = []
wrongGuesses = []
guessed = []

def menu():
    os.system("cls")
    print("HANGMAN: WARHAMMER EDITION!")
    print()
    print("SUBROUTINE EDITION")
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
        else: print("Invalid input, try again.")
    return lives
    
def game(lives):
    os.system("cls")
    
    while lives > 0:                       
        letter = input(f"You have {lives} remaining attempts. Enter a letter: ").lower()        
        os.system("cls")
        if letter in guessed and letter not in word: 
            print("You incorrectly guessed this letter before.")
        elif letter not in guessed: 
            if letter in word:       
                print("You have chosen... wisely!")
                correctGuesses.append(letter)                
            elif letter not in word:
                print("You have chosen... poorly! You lose one life.")
                lives -=1
                wrongGuesses.append(letter)
                
        guessed.append(letter)
        
        allLetters = True
        for i in word:
            if i in guessed:
                print(i, end="")
            else:
                print("_", end="")
                allLetters = False
        print()

        if allLetters:
            print(f"You won with {lives} left!")
            break
        elif lives == 0:
            print(f"😹 EPIC FAIL 😹 The correct word was {word.capitalize()}")
            break

lives=menu()
game(lives)