#Day_7

tvShow = input("What is your favorite sitcom? ")
if tvShow.lower() == "friends":
  print("Great taste~")
  favCharacter = input("Who is your favorite character? ")
  if favCharacter == "Joy" or favCharacter == "Phoebe":
    print("Right answer!")
  else:
    print("Nah, Joy's the greatest")
elif tvShow.lower() == "the office":
  print("I didn't really like that one")
else:
  print("Cool")

print("\nNow let's move to Anime~")

anime = input("What is your favorite anime? ")
if anime.lower() in ["one piece", "naruto", "attack on titans", "hunter x hunter", "demon slayer", "bleach", "fullmetal alchemist", "conan", "death note", "one punch man", "your lie in april", "jujutsu kaisen", "tokyo ghoul"]:
  print("That's a famous one huh.")

else:
  print("Impressed you know that one.")
  char = input("Name any character then ")
  if char == "Nami":
    print("Woah correct!")
  else:
    print("Wronggg u ain't otakuu.")