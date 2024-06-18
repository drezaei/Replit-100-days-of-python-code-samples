import os, random, time

min_num=1
max_num=144
rounds = 1

input("My turn to guess your number. This time, YOU think of a number, from 1 to 144, and I have to guess it. Hit Enter once you have thought of a number.")
print()

while True:
    guess = random.randint(min_num,max_num)
    question = input (f"I'm guessing your number is {guess}. Am I too high, too low, or am I correct?   ")

    if question in ["h","high"]:
        rounds +=1
        max_num = guess -1

    elif question in ["l","low"]:
        rounds +=1
        min_num = guess +1

    elif question in ["correct"]:
        if rounds == 1:
            print("Got it in one? I'm psyhic!")
        elif rounds >= 2:
            print(f"Nicely done (by me), I got it in {rounds} rounds")


