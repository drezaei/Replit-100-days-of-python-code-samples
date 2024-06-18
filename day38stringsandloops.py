roygbiv = ["r", "o", "y", "g", "b", "i", "v", " "]

while True:
    sentence = input("Type the sentence you want to 🌈 \033[91mR\033[0mA\033[94mI\033[0mN\033[94mB\033[0mO\033[34mY\033[33mF\033[91mY\033[0m🌈:\n>   ")
    print("")

    for letter in sentence:
        if letter.lower() in roygbiv:
            if letter.lower() == "r":
                print('\033[91m', end='')  # Red
            elif letter.lower() == "o":
                print('\033[38;5;208m', end='')  # Orange (sort of)
            elif letter.lower() == "y":
                print('\033[33m', end='')  # Yellow
            elif letter.lower() == "g":
                print('\033[32m', end='')  # Green
            elif letter.lower() == "b":
                print('\033[34m', end='')  # Blue
            elif letter.lower() == "i":
                print('\033[94m', end='')  # Indigo
            elif letter.lower() == "v":
                print('\033[35m', end='')  # Violet
            elif letter.lower() == " ":
                print('\033[0m', end='')   # Resets at space, hopefully

        print(letter, end='')

    print('\033[0m')  # Reset color at the end
    print("")







# Reset: \033[0m (Resets all formatting)

# Regular Colors:

# Red: \033[31m
# Green: \033[32m
# Yellow: \033[33m
# Blue: \033[34m
# Magenta: \033[35m
# Cyan: \033[36m
# White: \033[37m
# Orange: \033[38;5;208m

# Bright (Bold) Colors:
# Bright Black: \033[90m
# Bright Red: \033[91m
# Bright Green: \033[92m
# Bright Yellow: \033[93m
# Bright Blue: \033[94m
# Bright Magenta: \033[95m
# Bright Cyan: \033[96m
# Bright White: \033[97m
 
#ROYGBIV