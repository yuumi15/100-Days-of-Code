#Day_22

import random
print("Guess the number game!!\nChoose a numebr between 1 and 1,000,000\n")

num = random.randint(1, 1000000)
counter = 0

while True:
  counter +=1
  ans = int(input("Enter your guess: "))
  if ans > num:
    print("Too high")
  elif ans < num and ans > -1:
    print("Too low")
  elif ans == num:
    print("You got it! 🎉 only in", counter, "attempts")
    break
  elif ans < 0:
    print("Now you'll never know what the answer is > <")
    exit()
  else:
    print("Its not a number I recognize ??")
  