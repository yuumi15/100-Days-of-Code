#Day_6
 
print("Welcome to the Portal!\n")
username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == "ahmed" or username == "mark" or username == "sonia") and password == "password":
  print("Welcome", username, "! Happy to see you again~ Enjoy your day and your time on my lovely portal")

elif (username == "ahmed" or username == "mark" or username == "sonia") and password != "password":
  print("Wrong password, access denied!")

else:
  print("You are not allowed to access this portal! HOSTILE WE WA WE WAAA WEEE WAAAAAAAA")