from replit import audio
import random, time, os

colours_library = [31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96]
text = "My Brand New Music Player"
separator = "-"*25 
additional_lines = "\(1)Play Music\n(2)Quit\n"  # Add your additional lines here

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:  # Start taking user input and doing something with it
    input()


def splash_screen():
    lines = ["My", "Brand", "New", "Music", "Player"]

    for loading in lines:
        colours = random.choice(colours_library)
        os.system("cls")
        flashing_text = f"\033[{colours}m{loading}\033[0m"
        print(flashing_text, end='', flush=True)
        time.sleep(0.75)

def main_menu():
    while True:
        colours = random.choice(colours_library)
        os.system("cls")
        flashing_text = f"\033[{colours}m{text}\033[0m"
        flashing_seperator= f"\033[{colours}m{separator}\033[0m"
        flashing_lines = f"\033[{colours}m{additional_lines}\033[0m"
        print(flashing_text, end='\n', flush=True)
        print(flashing_seperator, end='', flush=True)
        input(flashing_lines, end='', flush=True)
        time.sleep(0.75)

        if input == "1":
            play()

        elif input == "2":
            break
    


splash_screen()
main_menu()
