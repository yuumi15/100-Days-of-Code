#Day_34
#Am I really making progress or just
#procrastinating and wasting my time..?

import os, time
listOfEmail = []

def prettyPrint():
  os.system("cls") 
  print("listofEmail") 
  print()
  for i in range(len(listOfEmail)): 
    print(f"{i}: {listOfEmail[i]}") 
  time.sleep(2)

def spamPrint():
  os.system("cls") 
  for i in range(len(listOfEmail)): 
    print()
    print(f"Email {i}:\nDear{listOfEmail[i]}, \nIt has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.\n\nLove and hugs,\nIan Spammington III")
    print()
  time.sleep(10)
  
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3": 
    prettyPrint()  
  elif menu == "4": #The Challenge
    spamPrint()
    
  time.sleep(1)
  os.system("cls")