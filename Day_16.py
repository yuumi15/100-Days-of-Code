#Day_15
#Fill in the blank

print("Fill in the blank lyrics!")
i = 1
while True:
  mis = input("So, it's always back to you again, always back to you_______you keep me on the run: ")
  if mis == "my friend":
    break
  else:
    print("Not quite, try again")
    i +=1
print("Wow you got itttt yahoo\nIt only took you", i, "attempts")