print("MULTIPLICATION TIME!")
key=int(input("What multiple should we test you on?  "))
print()

min_num=1
max_num=12
points=0

for i in range(min_num,max_num+1):
    question=int(input(f"{i} x {key} = "))
    if question == (i*key):
        points+=1

    
print(f"You scored {points} out of a possible {max_num}")
        