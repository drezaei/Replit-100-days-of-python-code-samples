#3x3 BINGO CARD
#| x | y | z |
#-------------
#| x | y | z |
#-------------
#| x | y | z |

import random, os

topleft =       random.randint(0, 90)
topcentre=      random.randint(0, 90)
topright=       random.randint(0, 90)

midleft=     random.randint(0, 90)
mididdle=   ("BINGO!")
midright=    random.randint(0, 90)

botleft=     random.randint(0, 90)
botmiddle=   random.randint(0, 90)
botright=    random.randint(0, 90)

separator=("----------------------")


card = [
    f"|  {topleft}  |  {topcentre}  |  {topright}  |",
    separator,
    f"|  {midleft}  |{mididdle}|  {midright}  |",
    separator,
    f"|  {botleft}  |  {botmiddle}  |  {botright}  |"
]

def bingo():
    while True:
      os.system("cls")
      print("BINGO CARD GENERATOR")
      print()
      print(card[0])
      print(card[1])
      print(card[2])
      print(card[3])
      print(card[4])
      print()
      ask = input("Enter 'N' for a new card, anything else will quit the program.\n").lower()
      if ask == "n":
            continue
      else:
            break
bingo()


#my2DList = [ ["Johnny", 21, "Mac"],
#             ["Sian", 19, "PC"],
#             ["Gethin", 17, "PC"] ]

#print(my2DList[0][0])
# This code outputs 'Johnny'. It's Johnny's name from list 0 (first square bracket), item 0 (second square bracket)

#print(my2DList[1][2])
# This code outputs 'PC'. It's Sian's computing preferene from list 1 (first square bracket), item 2 (second square bracket)