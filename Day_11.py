#Day_11
#Seconds in a year Calculator

leapOrNot = input("This is seconds-in-a-year calculator!!\nIf it's a leap year press 1, if not any normal key: ")

if leapOrNot == "1":
  print("There are", 366*24*60*60, "seconds in a year")
else:
  print("There are", 365*24*60*60, "seconds in a year")
  