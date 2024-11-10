#Day_15
#Kids Game - Animal Sound

print("Welcome to the Game!\nWhen you are done palying type --> yes\n")
while exit != "yes":
  ani = input("What animal do you want?: ")
  if ani.lower() == "cow":
    aniSound = "mooOoo"
    print("A", ani.lower(), "goes", aniSound)
  elif ani.lower() == "duck":
    aniSound = "kwaaak"
    print("A", ani.lower(), "goes", aniSound)
  else:
    aniSound = "yahahhh"
    print("A", ani.lower(), "goes", aniSound)
  exit = input("Exit?: ")
