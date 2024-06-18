#Enter the first number: 12
#Enter the second number: 8

#Sum: 20
#Product: 96
#Quotient: 1.5
#Remainder: 4
#Common Divisor: 4

import os

def asked_numbers():
    while True:
        num0=int(input("Enter your first number:    "))
        num1=int(input("Enter your second number:    "))
        return num0, num1

def num_propeties(num0, num1):

    os.system("cls")
    print(f"{num0} and {num1} together have the following properties")
    print("Sum: ",num0+num1)
    print("Product: ",num0*num1)
    print("Quotient: ",num0/num1)
    print("Remainder: ",num0%num1)
    print("Common Divisor: ",num0//num1)



num0, num1=asked_numbers()
num_propeties(num0, num1)