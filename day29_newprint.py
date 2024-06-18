import os, time

def user_text():
    clear_screen()
    text=input("Type your beautiful words here:\n")
    
    while True:
        colours=input("\nNow, what colour (blue, red, green, black, white, magenta, cyan, yellow) you want the text to appear in?\n").lower()
        if colours.lower() in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
            return text, colours
        else: print("\nThat's not on the list, try again!")
        time.sleep(1)
        clear_screen()

def user_print(text, colours):
    if colours == "red":
        print(f"\033[31m{text}\033[0m")

    elif colours == "black":
        print(f"\033[30m{text}\033[0m")

    elif colours == "green":
        print(f"\033[32m{text}\033[0m")

    elif colours == "yellow":
        print(f"\033[33m{text}\033[0m")

    elif colours == "blue":
        print(f"\033[34m{text}\033[0m")

    elif colours == "magenta":
        print(f"\033[35m{text}\033[0m")

    elif colours == "cyan":
        print(f"\033[36m{text}\033[0m")
    
    elif colours == "white":
        print(f"\033[37m{text}\033[0m")

    
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear') 



text, colours=user_text()
user_print(text, colours)

# Black: \033[30m
# Red: \033[31m
# Green: \033[32m
# Yellow: \033[33m
# Blue: \033[34m
# Magenta: \033[35m
# Cyan: \033[36m
# White: \033[37m