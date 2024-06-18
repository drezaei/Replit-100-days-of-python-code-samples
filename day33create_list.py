import os

myAgenda = []

def printList():
    print()
    for item in myAgenda:
        print(item)
    print()

def clearScreen():
    # Check the operating system and use the appropriate command to clear the screen
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

while True:
    item = input("What's next on the Agenda? 'Remove' will delete a previous entry: ")
    if item.lower() != "remove":
        myAgenda.append(item)
        clearScreen()
        printList()
    else:
        item = input("What do you want to remove? ")
        if item in myAgenda:
            myAgenda.remove(item)
            clearScreen()
            printList()
        else:
            print()
            print(f"{item} was not in the list")
