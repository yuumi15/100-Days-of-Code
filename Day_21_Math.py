#Day_21
#Math Game
import random

print("Welcome to Math Facts Game\n")
m = int(input("Enter your multiple: "))
score = 0

for i in range(3):
  x = random.randint(1, 12)
  print("")
  print(m, "X", x, "=")
  q = int(input())
  if q == m*x:
    print("Correct!")
    score +=1
  else:
    print("Wrong~ The correct answer is", m*x)

print("\nYour score is:", score)