#Day 27
#Character Generator

import os, time, random

def rollDice(side):
  result = random.randint(1, side)
  return result

def health():
  healthStat = ((rollDice(6) * rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6) * rollDice(8))/2)+12
  return strengthStat


while True:
  print("✦.── Character Builder ──.✦\n")
  
  name = input("\nName Your Character: ")
  type = input("Select Type (Human, Elf, Wizard, Orc): ")

  print()
  print(name)
  time.sleep(1)
  print("TYPE: ", type)
  time.sleep(1)
  print("HEALTH: ", health())
  time.sleep(1)
  print("STRENGTH: ", strength())
  time.sleep(1)
  print()
  new = input("Build New Character? (Y/N)")
  if new.lower() == "y":
    os.system("cls")
    continue
  elif new.lower() == "n":
    print("Alright, Bye")
    time.sleep(2)
    os.system("cls")
    break
  else:
    print("RIGHT BACK AT YOU") 
    time.sleep(2)
    os.system("cls")
    break