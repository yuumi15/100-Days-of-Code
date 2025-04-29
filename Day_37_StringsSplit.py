#Day 37
#Splitting Strings

print("STAR WARS NAME GENERATOR\n")

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
momName = input("Enter your mother's maiden name: ")
birthCity = input("Enter your birth city: ")


firstStar = firstName[0:3].capitalize() + lastName[0:2].lower()

lastStar = momName[0:2].capitalize() + birthCity[0:3].lower()


print(f"\nYour Start Wars name is {firstStar} {lastStar}")