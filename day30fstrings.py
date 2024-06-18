print("Using one word, desribe each day of the course so far.")

for i in range(1, 31):
  thought = input(f"Day {i}: ")
  print()

  if i == 1 or i == 21 or i == 31:
    suffix = "st"
  elif i == 2 or i == 22:
    suffix = "nd"
  elif i == 3 or i == 23:
    suffix = "rd"
  else:
    suffix = "th"

  sentence = (f"You just said the {i}{suffix} day of the course was {thought}")
  print(f" {sentence:^75}")
  print()