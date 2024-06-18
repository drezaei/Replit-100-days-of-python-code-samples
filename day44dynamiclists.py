#   Repeatedly ask the user what number comes up next.
#   Check the bingo card to see if the number picked matches one on the card.
#   If the bingo card is all 'X's, then the user has won.

#   Create a subroutine called createCard to clean up some of the code from Day 43.
#   Use a variable and loop to store how many x's there are on the card. Add one every time a number is replaced.
#   Check the variable every time to see if it has reached the magic winning number.

import random, os

separator = "-" * 25
numbers_sorted = []
bingo = "BINGO"

def random_numbers():
    raw_numbers0 = sorted(random.randint(0, 9) for _ in range(3))
    numbers_sorted.append(raw_numbers0)
    raw_numbers1 = sorted(random.randint(0, 9) for _ in range(2))
    numbers_sorted.append(raw_numbers1)
    raw_numbers2 = sorted(random.randint(0, 9) for _ in range(3))
    numbers_sorted.append(raw_numbers2)

    return raw_numbers0, raw_numbers1, raw_numbers2

def card_maker(numbers_sorted):
    card = [
        separator,
        f"|   {numbers_sorted[0][0]}   |   {numbers_sorted[0][1]}   |   {numbers_sorted[0][2]}   |",
        separator,
        f"|   {numbers_sorted[1][0]}   | {bingo} |   {numbers_sorted[1][1]}   |",
        separator,
        f"|   {numbers_sorted[2][0]}   |   {numbers_sorted[2][1]}   |   {numbers_sorted[2][2]}   |",
        separator,
    ]

    return card

def card_printer(card):
    for line in card:
        print(line)

def bingo_game():
    called = 0
    while True:
        banker = int(input("Number (0-9): "))
        for row in numbers_sorted:
            if banker in row:
                found = True
                for i in range(len(row)):
                    if row[i] == banker:
                        row[i] = "X"
                        called += 1

            if found:
                card = card_maker(numbers_sorted)
                os.system("cls")
                card_printer(card)

            if called == 8:
                print("BINGO! You win!")
                quit()
            

raw_numbers0, raw_numbers1, raw_numbers2 = random_numbers()
card = card_maker(numbers_sorted)
card_printer(card)
bingo_game()


#while True:
#  prettyPrint()
#  num = int(input("Next Number: "))
#  for row in range(3):
#    for item in range(3):
#      if bingo[row][item] == num:
#        bingo[row][item] = "X"

  