import random, os

random_words = ["hobbit", "ring", "wraiths", "fellowship", "gandalf", "aragorn", "sauron", "mordor", "rivendell", "gollum", "elrond", "orcs", "galadriel"]
counter = 0

todays_word = random.choice(random_words)


input("I know a word, a word related to Lord of the Rings. Guess the word. The fewer guesses the better. I will give one clue for each fail. Hit Enter to continue.")

while True:
    os.system("cls")
    os.system("cls")
    guess=input("The word is:   ").strip().lower()

    if guess != todays_word:
        counter += 1
        first_x_letters = todays_word[:counter]
        input(f"Sorry, that's wrong. The word I'm thinking of starts with {first_x_letters}.")
    
    elif guess == todays_word:
        os.system("cls")
        print(f"Well done, the word was indeed {todays_word.title()}. It took you {counter} guesses.")
        break

