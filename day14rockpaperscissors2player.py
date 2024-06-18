import os

P1Score = 0
P2Score = 0

round_number = 1


def ReadyPlayerNames():
    print("ROCK PAPER SCISSORS: MULTIPLAYER EDITION")
    print("-"*42)
    ReadyPlayer1=input("First player's name:    ").strip()
    ReadyPlayer2=input("Second player's name:   ").strip()
    input(f"Welcome {ReadyPlayer1} and {ReadyPlayer2}")
    return ReadyPlayer1, ReadyPlayer2

def RockPaperScissorsGame(ReadyPlayer1, ReadyPlayer2):
    from getpass import getpass as input

    while True:
        if P1Score < 3 and P1Score < 3:
            os.system("cls")    
            Player1Input=input(f"Round: {round_number}\n{ReadyPlayer1} selects (r)ock, (p)aper, or (s)cissors:\n").strip().lower()
            Player2Input=input(f"Round: {round_number}\n{ReadyPlayer2} selects (r)ock, (p)aper, or (s)cissors:\n").strip().lower()

            if Player1Input in ["rock", "paper", "scissors", "r", "p","s"] and Player2Input in ["rock", "paper", "scissors", "r", "p", "s"]:
                return Player2Input, Player1Input
                
            elif print(f"Invalid input from either {ReadyPlayer1} or {ReadyPlayer2}. Try again."):
                continue
        
        elif P1Score >2:
            print(f"{ReadyPlayer1} is the winner!")
            break

        elif P2Score >2:
            print(f"{ReadyPlayer2} is the winner!")


    


            
        



ReadyPlayer1, ReadyPlayer2 = ReadyPlayerNames()
RockPaperScissorsGame(ReadyPlayer1, ReadyPlayer2) 