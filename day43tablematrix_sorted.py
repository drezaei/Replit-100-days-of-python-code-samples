import random, os

separator = "-"*25
bingo= "BINGO"
raw_numbers = []

def rand():
    os.system("cls")
    raw_numbers = [random.randint(1, 9) for _ in range(9)]
    raw_numbers.sort()
    raw_numbers.append
    print("3x3 BINGO CARD GENERATOR")
    print()

    card = [
        separator,
        f"|   {raw_numbers[0]}   |   {raw_numbers[1]}   |   {raw_numbers[2]}   |",
        separator,
        f"|   {raw_numbers[3]}   | {bingo} |   {raw_numbers[4]}   |",
        separator,
        f"|   {raw_numbers[5]}   |   {raw_numbers[6]}   |   {raw_numbers[7]}   |",
        separator,
    ]

    for line in card:
        print(line)
        print()            

    query=input("Enter 'N' for a new card, any other input will close the program.\n").lower()
    if query == "n":
        rand()



rand()

#print(card[0])
#print(card[1])
#print(card[2])
#print(card[3])
#print(card[4])
#print(card[5])
#print(card[6])
#print(card[7])



#bingo = []

#def ran():
#  number = random.randint(1,90)
#  return number

#def prettyPrint():
#  for row in bingo:
#    print(row)

#numbers = []
#for i in range(8):
#  numbers.append(ran())

#numbers.sort()

#bingo = [ [ numbers[0], numbers[1], numbers[2]],
#          [ numbers[3], "BINGO", numbers[4] ],
#          [ numbers [5], numbers[6], numbers[7]]
#        ]

#prettyPrint()