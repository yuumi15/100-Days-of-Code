#Day 26

import os, time, pygame

def pause():
  pygame.mixer.pause()
  
def play():
  pygame.mixer.unpause()
  while True:
    stop_music = int(input("Press 2 to pause and return to main menu"))
    if stop_music == 2:
      pause()
    else:
      continue

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('Secret_Paradise.mp3')
sound.play()
pause()

while True:
  os.system("cls")
  print("~My Music Player~")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press any key to see menu again")
  
  option = int(input(""))
  if option == 1:
    print("Playing you some tunes!")
    play()
  elif option == 2:
    exit()
    os.system("cls")
  else:
    continue