import random

def dice_values():
    d6 = random.randint(1,6)
    d8 = random.randint(1,8)
    return d6, d8

def dice_rolls(d6, d8):
    high = d8*d8
    med = d8*d6
    low = d6*d6
    return high, med, low

def character_gen():
    d6, d8= dice_values()
    high, med, low = dice_rolls(d6,d8)
    name=input("Name:   ")
    
    while True:
        career_question=int(input("1. Warrior\n2. Rogue\n3. Wizard"))
        if career_question == 1:
            career_chosen = "Warrior"
            hp= high
            mp= low
            break
        
        elif career_question == 2:
            career_chosen = "Rogue"
            hp= med
            mp= med
            break

        elif career_question == 3:
            career_chosen = "Wizard"
            hp = low
            mp = high
            break

        else:
            continue

    print(f"{name} the {career_chosen} has {hp} hit-points, and {mp} magic-points.") 


character_gen()