#Day_19
#Loan Calculator

print("<<< Welcome to the LOAN CALCULATOR >>>\n")
money = float(input("Enter the amount of money: "))
interest = float(input("Enter the interest rate (e.g. If 5% type 0.05): "))
print("")            

for i in range(10):
  money = money + (money * interest)
  print("Year", i, "is", round(money, 2))
print("\nYou paied", round(money,2), "in interest!")