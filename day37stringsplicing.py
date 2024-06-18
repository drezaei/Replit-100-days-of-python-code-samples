import random

print("YOUR STAR WARS FORCE USER NAME")
print("")

titles = ["Darth", "Inquisitor", "Dark Lord", "Grand Master", "Padawan", "Jedi Knight"]
random_title = random.choice(titles)

first = input("Enter your first name:  ")
last = input("Enter your last name:  ")
pet = input("Enter the name of your favourite pet:  ")
city = input("Enter the town/city you were born in:  ")
print("")

jedi1 = first[0:3] + last[0:3]
jedi2 = pet[0:2] + city[-3:]
first_name = f"{jedi1.capitalize()}"
last_name = f"{jedi2.capitalize()}"

print(f"Your name in the Star Wars universe is '{random_title} {first_name} {last_name}'.")