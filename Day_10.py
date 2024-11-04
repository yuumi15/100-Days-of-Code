#Day_10
#Restaurant Tip Calculator

myBill = float(input("What was the bill? "))
tip = float(input("What % do you want to tip? "))
numberOfPeople = int(input("How many people involved? "))
tip = myBill*tip/100
answer = (myBill + tip) / numberOfPeople

print("\nTotal Bill after tip is", myBill+tip)
print("You all owe", round(answer, 2))
