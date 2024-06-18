import os 

while True:
    print("GRADE CALCULATOR")
    print()
    subject=input("Name of the subject you want graded:\n")
    os.system("cls")
    max_score=(int(input("What is the maximum possible score you could get in the test:\n")))
    os.system("cls")
    actual_score=(int(input("What score did you actually get:\n")))
    os.system("cls")
    percent=actual_score/max_score*100

    if percent ==100:
        print(f"You scored {percent}% in {subject}")
        input("You just got lucky with that test, A++ for a perfect score (apparently)")
    elif 90 <= percent <= 99:
        print(f"You scored {percent}% in {subject}")
        input("Looks like being a nerd paid off, you got a A+!")
    elif 80 <= percent <= 89:
        print(f"You scored {percent}% in {subject}")
        input("Not bad, but not good either, B")
    elif 70 <= percent <= 79:
        print(f"You scored {percent}% in {subject}")
        input("Mediocre, nothing to be proud of. You got a C.")
    elif 60 <= percent <= 69:
        print(f"You scored {percent}% in {subject}")
        input("Not even average, you 'passed', I suppose. D at best")
    elif 0 <= percent <= 59:
        print(f"You scored {percent}% in {subject}")
        input("😹😹😹GET MOGGGED😹😹😹")
    else:
        input("You can't even")

    os.system("cls")


    



#Letter Grade	Percentage
#A+	90-100
#A	80-89
#B	70-79
#C	60-69
#D	50-59
#U	under 50


