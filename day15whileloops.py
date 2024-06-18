import random

dog = ["🐶", "🐕", "🐩", "🐕‍🦺"]
cat = ["🐱", "🐱‍🚀", "🐱‍👓", "🐱‍🐉", "🐱‍💻", "🐱‍🏍", "🐱‍👤", "🙀", "😿", "😾", "😺", "😻", "😼", "😽"]
fish = ["🐠", "🐟", "🐡", "🐬"]
bird = ["🐦", "🦅", "🦆"]
horse = ["🐎", "🏇", "🐴"]
monkey = ["🐵", "🙈", "🙉", "🙊"]
rabbit = ["🐇", "🐰"]
fox = ["🦊"]
wolf = ["🐺"]
pig = ["🐖"]
cow = ["🐄", "🐮"]
elephant = ["🐘"]
bear = ["🐻"]
deer = ["🦌"]
pussy = ["😹😹😹😹😹😹😹😹"]
fish = ["🐠", "🐟", "🐡"]
cow = ["🐮"]

animal = input("I'll show you an emoji of most common pets or farm animals. Tell me what animal you want to see: ").strip().lower()

if animal in ["dog", "puppy", "doggo", "pup"]:
    print(random.choice(dog))
elif animal in ["cat", "kitten", "kitty"]:
    print(random.choice(cat))
elif animal == "pussy":
    print(random.choice(pussy))
elif animal == "cow":
    print(random.choice(cow))
elif animal in ["rabbit", "wabbit"]:
    print(random.choice(rabbit))
elif animal == "fox":
    print(random.choice(fox))
else:
    print("Sorry, I don't have an emoji for that animal.")
