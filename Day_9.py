#Day_9
#Generation Identifier

year = int(input("Which year were you born? "))

if year >= 1883 and year <= 1900:
  print("You are dead! ~Lost Generation~ Do you guys have internet access down there?")

elif year >= 1901 and year <= 1927:
  print("You are the Greatest Generation! Still alive? Not for long~")

elif year >= 1928 and year <= 1945:
  print("You are the Silent Generation! Imprssed you are here.")

elif year >= 1946 and year <= 1964:
  print("Boomers! Such a wild youth you had!")

elif year >= 1965 and year <= 1980:
  print("You are Generation X! You are the best generation!")

elif year >= 1981 and year <= 1996:
  print("Millinial!")

elif year >= 1997 and year <= 2010:
  print("GenZ, Just like me!")

elif year >= 2011:
  print("Generation Alpha! The Tech Savys")