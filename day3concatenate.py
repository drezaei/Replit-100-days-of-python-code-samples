#We have learned enough skills for a simple, but cool, project!

#Remember when you were a kid and thought the ideal dinner would just be all your favorite things mixed in a bowl? 
#How did that Nutella Mac & Cheese taste? Well - let's come up with a recipe generator to build us an amazing dish for today's evening meal!

#You will need to:

#Create these as a variable:
#A type of food
#A type of plant
#A method of cooking
#A word to describe burned food
#A household item

import os, random

print("LE TOTALLY RAND0M DISH GENERATOR🤪")

food=input("What common food to use as the basis for this recipe?\n")

plant=input("Name a plant, any plant really tbh?\n")

cook=input("Pick a method of cooking or heating something.\n")

adjective=input("Type in the first adjective that comes to mind:\n")

householdItem=input("Nearest item to your left is a what\n")

os.system("clear")

wordBank1=["feasting", "gorging", "devouring", ]
word1=random.choice(wordBank1)

wordBank2=["shredded", "grated", "diced", "minced"]
word2=random.choice(wordBank2)


print(f"For tonight, we well be {word1} on:", food, f"with {word2}", plant + ", which we will", cook, "until it is nice and", adjective + ". We'll top it off with some", householdItem,".")
