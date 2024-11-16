#Day_24
import random

print("Infinity Dice 🎲\n")
sideNum = int(input("How many sides? "))

def roll_dice(side):
  print("You rolled", random.randint(1, side))

roll_dice(sideNum)
while True:
  ans = input("\nRoll again? [yes-no] ")
  if ans.lower() == "yes":
    roll_dice(sideNum)
  else:
    break