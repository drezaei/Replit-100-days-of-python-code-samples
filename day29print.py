import os

def user_text():
    words = input("Enter a bunch of words: ")
    freq = int(input("How many times do you want to repeat the words? "))
    print("")

    while True:
        print("How would you like to format the words?")
        format_option = int(input("1 for space, 2 for comma, 3 for space & comma, 4 for new line, 5 for tab, or 6 for vertical tab. "))
        if format_option not in [1, 2, 3, 4, 5, 6]:
            print("Please enter a valid number.")
        else:
            break

    while True:
        color = input("Would you like to change text color? We have a choice of red, green, blue, and 'none' if you prefer to leave as default: ").lower()
        if color not in ["red", "green", "blue", "none"]:
            print("Please enter a valid color.")
        else:
            break
    
    return words, freq, format_option, color

def apply_color(color):
    if color == "red":
        return '\033[91m'  # ANSI escape code for red
    elif color == "green":
        return '\033[92m'  # ANSI escape code for green
    elif color == "blue":
        return '\033[94m'  # ANSI escape code for blue
    else:
        return ''

def reset_color():
    return '\033[0m'  # ANSI escape code for resetting color

def output(words, freq, argument, color):
    os.system('cls')

    while True:
        for i in range(freq):
            print(apply_color(color), end="")

            if argument == 1:
                print(words, end=" ")
            elif argument == 2:
                print(words, end=",")
            elif argument == 3:
                print(words, end=", ")
            elif argument == 4:
                print(words)
            elif argument == 5:
                print(words, end="\t")
            elif argument == 6:
                print(words, end="\v")

            print(reset_color(), end="")

        print("")
        print("")
        repeat_input = input("Again? (yes/y to repeat, any other key to exit): ")
        if repeat_input.lower() in ["yes", "y"]:
            words, freq, argument, color = user_text()
            os.system('cls')
        else:
            print("Goodbye")
            break

words, freq, format_option, color = user_text()
output(words, freq, format_option, color)


#TextColors:
#    RED = '\033[91m'
#    GREEN = '\033[92m'
#    YELLOW = '\033[93m'
#    BLUE = '\033[94m'
#    MAGENTA = '\033[95m'
#    CYAN = '\033[96m'
#    WHITE = '\033[97m'

# ANSI escape code for resetting color
# RESET = '\033[0m'