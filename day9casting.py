#    To convert Celsius to Fahrenheit: F = C * 9/5 + 32
#    To convert Fahrenheit to Celsius: C = (F - 32) * 5/9

import time

print("Celsius/Fahrenheit Converter")

def cORf():
    while True:
        unit = input("Change from (C)elsius to Fahrenheit, or (F)ahrenheit to Celsuis:  ").strip().lower()
        if unit in ["c", "celsius", "f", "fahrenheit"]:
            return unit
        else:
            print("Invalid input, try again.")
            time.sleep(1)

def convert(unit):
    while True:
        temp=int(input("What is the temp:   "))
        if unit in ["c","celsius"]:
            c2f=temp * 9/5 + 32
            print(f"{temp}{unit[0].upper()} is {c2f} Fahrenheit")
            break

        elif unit in ["f", "fahrenheit"]:
            f2c=(temp -32) * 5/9
            print(f"{temp}{unit[0].upper()} is {f2c} Celsuis")
            break

        else:
            print("Invalid input, try again.")
            time.sleep(1)
            continue


unit = cORf()
convert(unit)