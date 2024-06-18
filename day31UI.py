import random, os


def colour_change():
  number = random.randint(1, 7)
  if number == 1:
    colour = "\033[91m"  # Red
  elif number == 2:
    colour = "\033[92m"  # Green
  elif number == 3:
    colour = "\033[93m"  # Yellow
  elif number == 4:
    colour = "\033[94m"  # Blue
  elif number == 5:
    colour = "\033[95m"  # Magenta
  elif number == 6:
    colour = "\033[96m"  # Cyan
  else:
    colour = "\033[97m"  # Default
  return colour

colour = colour_change()

print(f"{colour: ^46}⚡⚡   LINAMP  ⚡⚡\033[0m")
print(f"{colour: ^40}IT REALLY WHUPS THE ALPACA'S BUTT 🦙\033[0m")
print("")
print("")
print(f"{colour: >10}⏯      Amie Doherty: For Whom The Bells Toll\033[0m")
print(f"{colour: >11}      Blue Eye Samurai Soundtrack (2023) \033[0m")
print()
print(f"{colour: ^35}⏭      Junkie XL: Brothers In Arms\033[0m")
print(f"{colour: ^36}      Mad Max Fury Road Soundtrack (2015)\033[0m")
print()
print(f"{colour: ^55}⏹      Track: 2:40 / 5:14 \033[0m")
print(f"{colour: ^56}      Playlist: Badass Anthems \033[0m")

#'\033[91m', #red,
#'\033[92m', #green,
#'\033[93m', #yellow
#'\033[94m', #blue
#'\033[95m', #magneta
#'\033[96m', #cyan
#'\033[97m', #white
