#Day_38
#Rainbow text

def ChangeColor(letter):
  if letter.lower() == 'y':
    print('\033[33m', end='') #yellow
  elif letter.lower() == 'r':
    print('\033[31m', end='') #red
  elif letter.lower() == 'b':
    print('\033[34m', end='') #blue
  elif letter.lower() == 'g':
    print('\033[32m', end='') #green
  elif letter.lower() == 'p':
    print('\033[35m', end='') #pink

  
myString = input("Input your favourite quote: ")
for letter in myString:
    ChangeColor(letter)
    print(letter, end="")