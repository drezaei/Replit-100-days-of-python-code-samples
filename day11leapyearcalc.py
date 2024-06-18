year = int(input("What year do you want to check? "))

while True:
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
    print("This means there was approximately", 60*60*24*366, "seconds in", year)    
    break  
  
  else:

    print(f"{year} is not a leap year.")
    print("This means there was approximately", 60*60*24*365, "seconds in", year)    
    break