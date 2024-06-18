#Have a menu that asks if you want to add, view, move or edit a 'to do'.

#If you choose 'add' then the system should:

#Prompt you to input what the to do is, when it is due by and the priority (high, medium or low).

#Add the 'to do' to the list.

#'View' should give two options:
#View all - shows all 'to dos' with a pretty print.
#View priority - allows you to search for high, medium or low priority and only see matching tasks.

#'Edit' allows you to change any of the information within one of the 'to dos'.

#'Remove' lets you completely remove a 'to do' when it is 'to done'.

#Use a separate subroutine for add, view, edit, and remove.

#Clear the console before viewing a new entry.

#Use a while True loop to call the subroutines and display the menu.

import os, time

my_todo = []

def main_menu():
    os.system("cls")
    while True:
        print("DAVID'S FIRST TO-DO LIST PROGRAM")
        print()
        option=input("(A)dd entries\n(V)iew entries\n(R)emove entries\n(E)dit entries\n")    
        if option in ["a","add"]:
            add()
        elif option in ["v","view"]:
            view()
        elif option in ["remove","r"]:
            remove()
        elif option in ["edit","e"]:
            edit()

def add():
    os.system("cls")
    task=input("Task:   ")
    monthDue=input("Month due:   ").strip().lower()
    month=monthDue[:3]
    while True:
        importance=input("Select level of importance:\n(H)igh\n(M)edium\n(L)ow\n").strip().lower()
        if importance in ["high", "hig", "hi", "h"]:
            priority = "high"
        elif importance in ["medium", "med","me","medi","mediu","m"]:
            priority = "medium"
        elif importance in ["low","lo","l"]:
            priority = "low"
        else:
            print("Try again")
            continue
        
        entries=[task,month,priority]
        my_todo.append(entries)
    
        repeat=input("Add a new task?   ")
        if repeat in ["yes","y"]:
            os.system("cls")
            continue
        else:
            os.system("cls")
            break


def view():
    while True:
        question=input("Do you want to see:\n(A)ll the entries\n(S)orted by month\n(H)igh priority only\n(M)edium priority only\n(L)ow priority only").strip().lower()

        if not my_todo:
            print("Nothing here yet.")
            break
        
        if question in ["all", "a"]:
            print("TASKS:")
            for entries in my_todo:
                print(f"Task: {entries['task']}")
                print(f"Due Date: {entries['month']}")
                print(f"Priority: {entries['priority']}")
                print("-" * 20)
            break  # Exit the loop after displaying tasks

        


def remove():
    print("Still working on it")
def option():
    print("Still working on it")
def edit():
    print("Still a WIP")

main_menu()



#Menu
    #Add
        #add entry 
            #task
            #due date
                #jan-dec or completed
            #priority
                #high
                #medium
                #low
    #View
        #view all (alphabetical? by order you put them in?)
        #view by date (nearest to jan goes to the top, completed tasks ignored)
        #view by priority
            #show only high
            #show only medium
            #show only low
    #Remove
        #move task to completed
        #just delete task for good
    #Edit
        #edit task name, priority, date.