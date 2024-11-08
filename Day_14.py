#Day_14
#Rock-Paper_Scissor Game
from getpass import getpass as input #to make the input hidden for secrecy
print("E P I C    🪨  📄 ✂️    B A T T L E")
print("Enter R, P or S for Rock, Paper, or Scissors simultanously\n")

#1st Player input
firstPlayer = input("1st player ENTER YOUR MoOoVE: ")
while firstPlayer != "R" and firstPlayer != "S" and firstPlayer != "P":
  firstPlayer = input("Invalid move, Enter again (R, P, S): ")

#2nd Player input
secondPlayer = input("2nd player GoOoOoo: ")
while secondPlayer != "R" and secondPlayer != "S" and secondPlayer != "P":
  secondPlayer = input("Invalid move, Enter again (R, P, S): ")

#Game logic
if firstPlayer == secondPlayer:
  print("Tie~")
  exit()
elif firstPlayer == "R" and secondPlayer == "S":
  print("First Player Won!! 11111")
elif firstPlayer == "R" and secondPlayer == "P":
  print("Second Player Won!! 22222")
elif firstPlayer == "S" and secondPlayer == "R":
  print("Second Player Won!! 22222")
elif firstPlayer == "S" and secondPlayer == "P":
  print("First Player Won!! 11111")
elif firstPlayer == "P" and secondPlayer == "R":
  print("First Player Won!! 11111")
elif firstPlayer == "P" and secondPlayer == "S":
  print("Second Player Won!! 222222")
  
print("CongratuulatiooOon 🎉🎉🎉 ✧｡٩(ˊᗜˋ )و✧*｡")




