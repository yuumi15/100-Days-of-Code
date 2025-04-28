#Day 36
#Manimpulating Strings
#Easy stuff i already know but lets keep the streak

listOfNames = []

def printList():
  print()
  for i in listOfNames:
    print(i)
  print()


while True:
  firstName = input("Enter your first name: ").strip().capitalize()
  lastName = input("Enter your last name: ").strip().capitalize()

  name = f"{firstName} {lastName}"
  if name not in listOfNames:
    listOfNames.append(name)
  else:
    print("\nERROR: Duplicate name")
  printList()