gatekeeper=input("So you say you're a Warhammer fan. Tell me, which Warhammer setting is the best?").lower().strip()

if gatekeeper == "warhammer fantasy":
  print("Objectively the correct answer. But I have one follow up question to test your knowledge.")
  test=input("Which of these is a character in Warhammer Fantasy:\n1)Malus Darkblade\n2)Arkhan Land\n3)Lord-Celestant Something Something")
  if test == "1":
    print("Correct! You are a true fan.")
  elif test == "2":
    print("Incorrect. You are not a true fan. Poser.")
  elif test == "3":
    print("Ding Dong You're Wrong.")
  else:
    print("That's not an option. You're not a true fan.")

elif gatekeeper in ["warhammer 40k", "warhammer 40000", "warhammer 40,000"]:
  print("Go home and play with your Spess Mahreens minis, loser.")

elif gatekeeper == "age of sigmar":
  print("You and I both know that's a terrible setting...")

else:
  print("Sorry, I don't speak nonsense.")