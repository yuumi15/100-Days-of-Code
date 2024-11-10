#Day_17
#Rock-Paper_Scissor Game ENHANCED Version
from getpass import getpass as input #to make the input hidden for secrecy
print("E P I C    🪨  📄 ✂️    B A T T L E")
print("Enter R, P or S for Rock, Paper, or Scissors simultanously\n")

score1 = 0
score2 = 0
while score1 < 3 and score2 < 3:
  
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
    print("Tie~\nPlay Again!\n")
  elif (firstPlayer == "R" and secondPlayer == "P") or (firstPlayer == "S" and secondPlayer == "R") or (firstPlayer == "P" and secondPlayer == "S"):
    print("Second Player Won this round!!\n")
    score2 +=1
  else:
    print("First Player Won this round!!\n")
    score1 +=1

print("Score: ", score1, " - ", score2)
winner = "First Player" if score1 > score2 else "Second Player"
print("CongratuulatiooOon",winner ,"🎉🎉🎉 ✧｡٩(ˊᗜˋ )و✧*｡")




