print("Multiplication Generator")

num1=int(input("What number you want to multiply?    "))
num2=int(input("Up to what number?  "))

for i in range(1, num2+1):
  print(i, "x ", num1, "=", (i * num1))