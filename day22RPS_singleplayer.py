import random, os
name=input("Rock Paper Scissors: Single Player Edition\n\nYour name:    ").strip().title()
print(f"Welcome, {name}!")

hal_weapons = ["r","p","s"]
player_score = 0
hal_score = 0
rounds = 0

while True:
    hal=random.choice(hal_weapons)
    player_weapon=input("(R)ock, (P)aper or (S)cissors?").strip().lower()
    
    if player_weapon not in ["rock", "r", "paper", "p","scissors","s"]:
        print("Invalid input, try again.")
        print()



    elif player_weapon in ["rock","r"] and hal in ["r"]:
        print(f"Draw! Both {name} and HAL picked rock. No points either way.")
        rounds+=1
        print()

    elif player_weapon in ["paper","p"] and hal in ["p"]:
        print(f"Draw! Both {name} and HAL picked paper. No points either way.")
        rounds+=1
        print()
    
    elif player_weapon in ["scissors","s"] and hal in ["s"]:
        print(f"Draw! Both {name} and HAL picked scissors. No points either way.")
        rounds+=1
        print()



    elif player_weapon in ["rock","r"] and hal in ["p"]:
        print(f"Oh no! HAL's paper covers {name}'s rock! One point to HAL.")
        hal_score +=1
        rounds+=1
        print()

    elif player_weapon in ["paper","p"] and hal in ["s"]:
        print(f"Oh no! {name}'s paper was cut up by HAL's scissors! One point to HAL.")
        hal_score +=1
        rounds+=1
        print()

    elif player_weapon in ["scissors","s"] and hal in ["r"]:
        print(f"Oh no! {name}'s scissors were crushed by HAL's mighty rock! One point to HAL.")
        hal_score +=1
        rounds+=1
        print()    



    elif player_weapon in ["rock","r"] and hal in ["s"]:
        print(f"Oh yes! {name}'s rock crushes HAL's scissors! One point to {name}.")
        player_score +=1
        rounds+=1
        print()

    elif player_weapon in ["paper","p"] and hal in ["r"]:
        print(f"Oh yes! {name}'s paper covers up HAL's rock! One point to {name}.")
        player_score +=1
        rounds+=1
        print()

    elif player_weapon in ["scissors","s"] and hal in ["p"]:
        print(f"Oh yes! {name}'s scissors cuts up by HAL's mighty rock! One point to {name}.")
        player_score +=1
        rounds+=1
        print()    


    
    if player_score == 3:
        print(f"{name} was the victor today, defeating their AI opponent in {rounds} rounds!")
        break

    if hal_score == 3:
        print(f"HAL was the victor today, defeating {name} in {rounds} rounds!")
        break