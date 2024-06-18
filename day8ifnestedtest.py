import os, time, random

bank=["Telescope", "Pineapple", "Hammer", "Umbrella", "Bicycle", "Cloud", "Stapler", "Ocean", "Backpack", "Candle", "Giraffe", "Piano"]

def greetings():
  question = input("What is your name? ").strip().title()
  os.system("cls")
  print(f"Greetings, {question}.")
  print()
  input("OK, so forget about the affirmation/insult generator thingy, we're going to test your memory here. I'm going to show you three random words, and you have to remember them. Press enter when you're ready.")
  os.system("cls")
  
def countdown():
  for i in range(5,0,-1):
    print(i)
    time.sleep(.25)
    os.system("cls")

def words():
    continues = 0
    chosen = random.sample(bank, 3)
    print(f"Your words are: {chosen[0]}, {chosen[1]}, and {chosen[2]}.")
    time.sleep(3)
    os.system("cls")
    while True:
        question0=input("Type one of the words you saw:  ").strip().title()
        question1=input("And another:   ").strip().title()
        question2=input("And finally, the last word:    ").strip().title()

        if question0 in chosen and question1 in chosen and question2 in chosen:
           print("Well done, you beaten the game.")
           break
        else:
           input("At least one of the answers were wrong, hit enter to try again.")
           continues +=1
           os.system("cls")
        
        if continues == 3:
           input("You failed too many times. Let's start again. Press enter.")
           continues = 0
           words()
 
    
      



greetings()
countdown()
words()