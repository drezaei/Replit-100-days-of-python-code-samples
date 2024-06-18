import time, os

names = []

def printList():
    os.system("cls")
    if not names:
        print("This list is empty, expand it by adding names. Duplicates will not be added.")
    else:
        print()
        count = 1
        for each in names:
            print(f"{count}: {each}")
            count+=1
        print("")

printList()

while True:
    print()
    first_name = input("First name:   ").strip().capitalize()
    last_name = input("Last name:     ").strip().capitalize()
    full_name = (f"{first_name} {last_name}")
    if full_name not in names:
       names.append(full_name)
    else:
        print("Duplicate entry, try a new name.")
        time.sleep(0.75)
    printList()
