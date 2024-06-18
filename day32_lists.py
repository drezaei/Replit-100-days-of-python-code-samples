import random
import statistics

#NumberList = []

def askUser():
#    global NumberList
    howManyNumbers = int(input("How large is this list of random numbers? "))
    biggestNumber = int(input("What's the biggest number in this list? "))

    random_numbers = [random.randint(1,biggestNumber) for _ in range(howManyNumbers)]
    NumberList = random_numbers
    return NumberList
    
    
def showUser(NumberList):
    print()
    print(f"unsorted: {NumberList}")
    NumberList.sort()
    print(f"sorted: {NumberList}")
    NumberMedian = statistics.median(NumberList)
    print(f"median: [{NumberMedian}]")
    NumberMode = statistics.mode(NumberList)
    print(f"mode: [{NumberMode}]")
    NumberList.reverse()
    print(f"reversed: {NumberList}")
    print()

NumberList = askUser()
showUser(NumberList)