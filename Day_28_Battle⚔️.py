#Day 28
#Battle

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


# def character(name, type):
#   name = input("\nName Your Character: ")
#   type = input("Select Type (Human, Elf, Wizard, Orc, Werewolf, Vampire): ")
#   print()
#   print(name)
#   time.sleep(1)
#   print("TYPE: ", type)
#   time.sleep(1)
#   print("HEALTH: ", health())
#   time.sleep(1)
#   print("STRENGTH: ", strength())
#   time.sleep(1)
  
# character(input("\nName Your Character: "), input("Select Type (Human, Elf, Wizard, Orc, Werewolf, Vampire): "))


print("✦.── Character Builder ──.✦\n")
  
name = input("\nName Your Character: ")
type = input("Select Type (Human, Elf, Wizard, Orc, Werewolf, Vampire): ")

print()
print(name)
time.sleep(1)
print("TYPE: ", type)
time.sleep(1)
health1 = health()
print("HEALTH: ", health1)
time.sleep(1)
strength1 = strength()
print("STRENGTH: ", strength1)
time.sleep(1)
  
print("\nWho are they battling?\n")
    
name2 = input("\nName Your Character: ")
type2 = input("Select Type (Human, Elf, Wizard, Orc, Werewolf, Vampire): ")

print()
print(name2)
time.sleep(1)
print("TYPE: ", type2)
time.sleep(1)
health2 = health()
print("HEALTH: ", health2)
time.sleep(1)
strength2 = strength()
print("STRENGTH: ", strength2)
time.sleep(2)  
os.system("cls")
round = 1

while True:
  print("\n⚔️ BATTLE TIME ⚔️\n")

  damage = abs(strength1 - strength2) +1
  ch1 = rollDice(6)
  ch2 = rollDice(6)
  
  if ch1 > ch2:
    winner = name
    loser = name2
    health2 -= damage
  elif ch2 > ch1:
    winner = name2
    loser = name
    health1 -= damage
  else:
    print("Their swords clash and they draw round", round)
    print()
  
    
  if round == 1:
    print(winner, "wins the first blow")
    print(loser, "takes a hit with", damage ,"damage")
  else:
    print(winner, "wins round", round)
    print(loser, "takes a hit with", damage ,"damage")

  print()
  print(name, "\n", health1, "\n")
  print(name2, "\n", health2, "\n")
  

  if health1 <= 0:
    print(name, "DIED!")
    print(name2, "destroyed", name, "in", round, "rounds!")
    break
  elif health2 <=0:
    print(name2, "DIED!")
    print(name, "destroyed", name2, "in", round, "rounds!")
    break
  else:
    print("And they're both standing for the next round!")
    time.sleep(2)
    os.system("cls")
    round += 1