#"Some trainers have no fear. To them, this is just one more challenge".

#Create a dictionary to store the details of your, ahem, MokéBeast.
#Ask the user to input the following details: name, type (earth, fire, air, water or spirit), special move, starting HP and starting MP. For now we're just taking in one set of values for one beast.
#Output the beast's details.
#Check the beast's type and change the color of the text accordingly. Fire is red, water is blue, air is white. You decide on the others.

#🥳 Extra points for getting all the inputs with just one input command and the split function.

#👉 IMPORTANT INFO - keep a note of where this Repl is, you'll need it in a couple of lessons' time.

import os, random, time

number01 = random.randint(1, 100)
number02 = random.randint(100, 999)
number03 = random.randint(100, 999)
bigDumbNum = (f"#{number01},{number02},{number03}")
date = ("X040024M3")
status = ("Status of Xenos: HERETIC. EXTERMINATE ON SIGHT.")  # No need to assign to a variable


def xenosDB():
  os.system("cls")
  print("Inqusitorial Cogitator WAKING UP")
  time.sleep(2)
  os.system("cls")
  print("ArchmagOS Linux")
  time.sleep(2)
  os.system("cls")
  print("Secreto magistratuum".upper())
  time.sleep(0.75)
  print("SECRETUM MAXIMUM. Tantum ad Oculum Ordo Xenos".upper())
  time.sleep(0.75)
  print("")
  print(f"Dated: {date}")
  print(f"Database Entry Number {bigDumbNum}")
  print()


def userInput():
  race = input("Designated name for the vile Xenos:    ")
  print("")
  while True:
    segmentum = input(
      "Select the Segmentum where First Contact took place:\n(1) Segmentum Solar\n(2) Segmentum Ultima\n(3) Segmentum Tempestus\n(4) Segmentum Obscurus\n(5) Segmentum Pacificus\n>   "
    )
    try:
      user_input = int(segmentum)
      if 1 <= user_input <= 5:
        if user_input == 1:
            user_segmentum = "\033[38;5;220mSegmentum Solar\033[0m"
        elif user_input == 2:
            user_segmentum = "\033[37mSegmentum Ultima\033[0m"
        elif user_input == 3:
            user_segmentum = "\033[94mSegmentum Tempestus\033[0m"
        elif user_input == 4:
            user_segmentum = "\033[31mSegmentum Obscurus\033[0m"
            
        else: user_segmentum = "\033[32mSegmentum Pacificus\033[0m"

        break  # Exit the loop if input is valid
      else:
        print("Invalid input. ")
    except ValueError:
      print("Invalid input. ")

  print("")
  planet = input("Name of planet where First Contact took place:  ")

  xenos = {"\nSUMMARY\n"
           
           "Name:": race,
           "ID number:": bigDumbNum, 
           "Segmentum:": user_segmentum, 
           "Planet:": planet,
           "Status:": status
           }

  for name, value in xenos.items():
    print(f"{name}  :   {value}")


xenosDB()
userInput()





#Start with your dictionary.
#You will need a for loop.
#Change the font color for the beast's type by using if statements.
#Change font color using print("\033[XXm", end="") - replace the XX with a color code.

##MokéBeast - The Non-Copyright Generic Beast Battle Game 
#Input your beast's name > Brian

#Input your beast's type > Earth

#Input your beast's special move > Flying bellyflop

#Input your beast's staring HP > 50

#Input your beast's staring MP > 20

# This text outputs in green
#Your beast is called Brian. It is an earth beast with a special move of Flying bellyflop