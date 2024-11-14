#Day_23
#Login_system
print("Welcome to the Login System!!\n")

def user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    while username != "username" or password != "password":
        print("\nWrong!! try again\n")
        return user()  # recursive call with return to recheck
    print("Welcome!") 

user()
