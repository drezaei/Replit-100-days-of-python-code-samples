import random
import os
import time

global_min_num = 1
global_max_num = 144
global_max_rounds = 12
global_sec_num = 12

def mainMenu():
    while True:
        os.system("cls")
        print("Number Guessing Game")
        print("-" * 21)
        menu = input("1) Least Efficient Algorithm\n2) Somewhat Efficient Algorithm\n3) Most Efficient Algorithm\n4) Change Values\n5) Display Current Values\n")

        if menu == "1":
            worstAlgorithm()
        
        elif menu == "2":
            middlingAlgorithm()
        
        elif menu == "3":
            bestAlgorithm()

        elif menu == "4":
            menuSettings()
        
        elif menu == "5":
            menuDisplay()

        else:
            continue

def menuSettings():
    global global_min_num, global_max_num, global_sec_num, global_max_rounds

    print()

    global_min_num = int(input("What's the minimum value on this range:    "))
    global_max_num = int(input("What's the maximum value on this range:    "))
    global_sec_num = int(input("What is your secret number:    "))
    global_max_rounds = int(input("How many times you want to run this algorithm:    "))

def worstAlgorithm():
    guesses = 0
    rounds = 0
    total_rounds = []

    min_num = global_min_num
    max_num = global_max_num
    max_rounds = global_max_rounds
    sec_num = global_sec_num
    collected_guesses = []

    os.system("cls")
    
    while rounds < max_rounds:
        guess = random.randint(min_num, max_num)
        if guess not in collected_guesses:
            collected_guesses.append(guess)
            guesses += 1
        
        if guess == sec_num:
            print(f"It took {guesses} attempts for me to guess your number.")
            total_rounds.append(guesses)
            collected_guesses = []
            guesses = 0
            rounds += 1
            time.sleep(1)
               
    total = sum(total_rounds)
    average = total / len(total_rounds)
    input(f"\nIn {max_rounds} rounds, it took on average {round(average, 2)} guesses.\nPress Enter to return to Menu:  ") 
    mainMenu()  

def middlingAlgorithm():
    global global_min_num, global_max_num, global_sec_num, global_max_rounds
    local_min_num = global_min_num
    local_max_num = global_max_num
    guesses = 0
    rounds = 0
    total_rounds = []
    collected_guesses = []

    os.system("cls")
        
    while rounds < global_max_rounds:
        guess = random.randint(local_min_num, local_max_num)
        
        if guess not in collected_guesses:
            collected_guesses.append(guess)
            guesses += 1
        
            if guess > global_sec_num:
                local_max_num = guess - 1

            elif global_sec_num > guess:
                local_min_num = guess + 1
            
            elif guess == global_sec_num:
                print(f"It took {guesses} attempts for me to guess your number.")
                total_rounds.append(guesses)
                collected_guesses = []
                guesses = 0
                rounds += 1
                local_max_num = global_max_num
                local_min_num = global_min_num
                time.sleep(1)

    total = sum(total_rounds)
    average = total / len(total_rounds)
    input(f"\nIn {global_max_rounds} rounds, it took on average {round(average, 2)} guesses.\nPress Enter to return to Menu:  ") 
    mainMenu()  

def bestAlgorithm():
    global global_min_num, global_max_num, global_sec_num, global_max_rounds
    local_min_num = global_min_num
    local_max_num = global_max_num
    guesses = 0
    total_rounds = []
    collected_guesses = []

    os.system("cls")
    
    guess_found = False
    
    while not guess_found:
        guess = (local_min_num + local_max_num) // 2
        
        if guess not in collected_guesses:
            collected_guesses.append(guess)
            guesses += 1
            
            if guess > global_sec_num:
                local_max_num = guess - 1

            elif global_sec_num > guess:
                local_min_num = guess + 1
                
            elif guess == global_sec_num:
                print(f"It took {guesses} attempts for me to guess your number.")
                guess_found = True
                time.sleep(1)

    total_rounds.append(guesses)
    total = sum(total_rounds)
    average = total / len(total_rounds)
    input(f"\nThis algorithm took {round(average, 2)} guesses.\nPress Enter to return to Menu:  ") 
    mainMenu()


def menuDisplay():
    os.system("cls")
    input(f"Minimum: {global_min_num}\nMaximum: {global_max_num}\nRounds: {global_max_rounds}\nSecret Number: {global_sec_num}\n")
    os.system("cls")



mainMenu()
menuSettings()
