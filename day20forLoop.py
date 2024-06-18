print("Loan Calculator")
currency=input("Currency:   ")
principal=int(input("How much money you burrowed:    "))
apr=float(input("Annual percentage rate:  "))
length=int(input("Length of the loan (in years):   "))
print()
total_interest = 0  

for i in range(length):
    
    principal+=(principal*apr)

    print(f"Year {i+1}: {currency}{round(principal,2)}")

