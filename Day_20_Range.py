#Day_20
#Range Generator

print("Welcome! What's your range?!\n")

start = int(input('Start at: '))
end = int(input('End before: '))
increment = int(input('Increment/decrement between values: '))
print("\nHere's your list:")
for i in range(start, end, increment):
  print(i)