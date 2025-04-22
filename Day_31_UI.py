#Day 31
#User Interafce?

title = "-  My Space  -"
text = "This text is supposed to be left alligned & colorful"
user = "Username:\n"
password = "Password:\n"
otherText = "Will it work?\n"

red = "\033[31m"
blue = "\033[34m"
green = "\033[32m"
noColor = "\033[0m"

print(f"Welcome to\n{blue}{title: ^50}{green}\n\n{text:>70}\n{red}{otherText:>50}")

print(f'{noColor}{user:^50}{password} \033[?25l', end="")





