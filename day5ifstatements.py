import os, time

print("Which programming languages is best suited for you.")
time.sleep(1)
os.system("clear")
print("Answer each question with 'yes' or 'no'")
print("")
score = {"Python": 0, "Rust": 0, "HTML 5": 0, "Unemployment": 0}

money = input("Do you like money? ").strip().lower()
if money in ["yes", "y"]:
    score["Python"] += 1
else:
    score["Unemployment"] += 1
os.system("clear")

power = input("Do you want to feel like a god? ").strip().lower()
if power in ["yes", "y"]:
    score["Rust"] += 1
else:
    score["Unemployment"] += 1
os.system("clear")

arbeit = input("Do you not want to actually program while appearing to 'programme' something?").strip().lower()
if arbeit in ["yes", "y"]:
    score["HTML 5"] += 1
else:
    score["Unemployment"] += 1
os.system("clear")

if score["Python"] > 0:
  print("You should learn Python.")

if score["Rust"] > 0:
  print("You should learn Rust.")

if score["HTML 5"] > 0:
  print("You should learn HTML 5.")

if score["Unemployment"] > 2:
  print("Maybe programming just isn't for you....")