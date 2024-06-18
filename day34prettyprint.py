import os, time

listOfEmail = []

def prettyPrint():
  clear_screen()
  print(listOfEmail)
  print()
  counter = 1
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter+=1
  time.sleep(1)
  clear_screen() 

def spam():
    clear_screen()
    for recipient in listOfEmail[:5]:
        print(f"""      
Subject: 🔮 Unleash the Power of Enchanted Potions! 🧙‍♂️

Dear {recipient},

Greetings from the Mystic Emporium! 🌟 Are you tired of your mundane existence? Do you long for the extraordinary and seek the secrets of ancient spells and enchanted elixirs?

🔮 Introducing our EXCLUSIVE collection of Magical Potions! 🌈

🌌 Potion of Invisibility: Vanish from sight and explore the realms unseen!
🌟 Elixir of Eternal Youth: Reverse the sands of time and embrace everlasting beauty!
💰 Prosperity Brew: Attract wealth and prosperity to your magical endeavors!
🌿 Herblore Essence: Enhance your herbalism skills and cultivate enchanted plants!

Act now, and you'll receive a FREE spellbook with your first purchase! ✨

But that's not all! Respond within the next 24 hours, and you could win a lifetime supply of Phoenix Feather Quills! 🦚

🌟 Don't miss this opportunity to transform your ordinary life into an extraordinary adventure! 🌟

To order, reply to this enchanted email with the codeword "MAGIC2024" and watch as your world unfolds with mystical wonders!

May your cauldron bubble with endless possibilities!

Best Regards,
Merlin's Magical Emporium 🧙‍♂️✨
""")
        time.sleep(1)
        clear_screen()

def menu():
    clear_screen()
    while True:
        print("SPAM R US")
        print("")
        option = input("1: Add email\n2: Remove Email\n3: Show Email\n4: Spam the first 5 email addresses!\n>  ")
        if option == "1":
            email = input("Email >  ")
            listOfEmail.append(email)
            clear_screen()
        elif option == "2":
            email = input("Email >  ")
            listOfEmail.remove(email)
            clear_screen()
        elif option == "3":
            prettyPrint()
        elif option == "4":
            spam()

def clear_screen():
  """Clears the screen depending on the operating system."""
  # Use 'cls' for Windows and 'clear' for Linux/macOS
  command = 'cls' if os.name == 'nt' else 'clear'
  os.system(command)

menu()
