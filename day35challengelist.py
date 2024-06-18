import os, time

toDo = []

def theList():
  os.system("cls")
  print(toDo)
  print()
  count = 1
  for activity in toDo:
    print(f"{count}: {activity}")
    count+=1
print("")
   
def addEntry():
    while True:
        os.system("cls")
        theList()
        entry = input("Type task here, entering 'q' will quit\n>  ")
        if entry.lower() == "q":
            os.system("cls")
            break                        
        elif entry in toDo:        
             print("Task already on the list.")
             time.sleep(0.5)
        else:    
            toDo.append(entry)
        
   
def removeEntry():
    os.system("cls")
    while True:
        theList()
        print("")
        removed = input("Type entry you want removed, entering 'q' will quit:\n>  ")
        if removed.lower() == "q":
            os.system("cls")
            break
        elif removed in toDo:
            print(f"{removed} has been removed.")
            time.sleep(0.75)
            toDo.remove(removed)
            theList()
        elif removed not in toDo:
            print(f"{removed} is not on the list")
            time.sleep(0.75)
            
def showEntry():
    os.system("cls")
    theList()
    input("\nPress Enter to return\n>  ")
    os.system("cls")

def editEntry():
    os.system("cls")
    theList()
    print("")
    entry = input("Type entry to edit, entering 'q' will quit:\n>  ")
    
    if entry == "q":
        os.system("cls")
        return
    elif entry not in toDo:
        print(f"{entry} is not on the list")
        time.sleep(0.75)
        os.system("cls")
        editEntry()        
    elif entry in toDo:
        new = input(f"Change {entry} to new task, 'q' will quit:\n>  ")
        if new in toDo:
            print(f"{new} is already on the list.")
            time.sleep(0.75)
            editEntry()
        elif new == "q":
            os.system("cls")
            theMenu()
        else:
            for i in range(len(toDo)):
                if toDo[i] == entry:
                    print(f"'{entry}' has been changed to {new}")
                    time.sleep(0.75)
                    toDo[i] = new
                    os.system("cls")
                    editEntry()
                            
def deleteAll():
    global toDo
    os.system("cls")
    sure = input("Are you sure? Type yes/y to confirm.\n>  ")
    if sure.lower() in ["y", "yes"]:
        print("ToDo list has been cleared.")
        time.sleep(0.75)
        toDo = []
        os.system("cls")
    else:
        theMenu()

def theMenu():
    while True:
        print("")
        print("\033[4mGetting Things Done\033[0m")
        print("")
        main_menu = input("1: Add task\n2: Remove task\n3: Show tasks\n4: Edit existing entry\n5: Delete the list  \n>  ")
        if main_menu == "1":
            addEntry()
        elif main_menu == "2":
            removeEntry()
        elif main_menu == "3":
            showEntry()
        elif main_menu == "4":
            editEntry()
        elif main_menu == "5":
            deleteAll() 


theMenu()