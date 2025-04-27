#Day 35
#Better ToDo List Manager

import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()


while True:
  menu = input("\n✦.──ToDoList Manager──.✦ \n\nDo you want to view, add, edit, or remove an item from the todo list?\n")
  
  if menu.lower()=="view":
    if len(toDoList) == 0:
      print("List is still empty, dude!")
    else:
      printList()
      
  elif menu.lower()=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
    print("Added SUCCESSFULLY")
    time.sleep(1)

  elif menu.lower()=="edit":
    item = input("What do you want to edit?\n")
    if item in toDoList:
      toDoList.remove(item)
      item = input("Edited Version: ")
      toDoList.append(item)
      print("~DONE~")
      
  elif menu.lower()=="remove":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      check = input("Are you sure you want to remove it? (yes/no)")
      if check.lower()=="yes":
        toDoList.remove(item)
        print("REMOVED SUCCESSFULLY")
      elif check.lower()=="no":
        print("Too late, its removed")
        time.sleep(0.5)
        print("haha jk, still there")
    else:
      print("Item is not there, You'll have to add ")

  time.sleep(2)
  os.system("clear")