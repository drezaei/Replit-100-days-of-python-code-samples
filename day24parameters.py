import random, os

def rolling(die, qty):
    print()
    for i in range(qty):
        roll = random.randint(1,die)
        print(f"The d{die} rolled {roll}")
    
    again=input("\nRoll again with new dice?  ").strip().lower()
    if again in ["y","yes"]:
        os.system("cls")
        die, qty = counting()
        rolling(die, qty)    
    else: 
        print("Thank you for playing!")


def counting():
    die=int(input("How many sides to this die?              "))
    qty=int(input("How many times we're rolling?            "))
    return die, qty


die, qty = counting()
rolling(die, qty)