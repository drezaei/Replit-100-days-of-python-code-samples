import random, os, time

random_num=random.randint(1,144)
counter=0

print("Number Guessing Game!")
input("I know a number, between 1 and 144. I will tell you if you're too high or low for each wrong answer. Try to get it done in as few guesses as possible. Hit Enter to continue")

while True:
    os.system("cls")
    guess=int(input("Guess: "))

    if guess == 420:
        print(f"{random_num}")
        counter -=1

    elif guess > random_num:
        print("\033[0;31mYou're too high.\033[0m")

    elif guess < random_num:
        print("\033[1;34mYou're too low.\033[0m")

    elif guess == random_num:
        print(f"Well done, the number was {random_num}. It took you {counter} guesses.")
        break

    else: 
        print("That's not even a valid number. Still counts as an attempt though!")

    counter +=1
    time.sleep(1)